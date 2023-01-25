# Image relating processing functions

import os
import random

import cv2
import numpy as np
import shapely.geometry

import sys
sys.path.append('../')

from ..facecctv_ai import utils
from ..facecctv_ai import geometry


class InvalidBoundingBox(Exception):
    pass

class CropException(Exception):
    pass

def scale_image(image, size):

      # Scale input inage so that the largest dimension is equal to size

      smallest_dimension = image.shape[0] if image.shape[0] < image.shape[1] else image.shape[1]
      scale = size / smallest_dimension

      # Dimensions have to be flipped for cv2.resize 
      target_shape = (round(scale * image.shape[1]), round(scale * image.shape[0]))
      return cv2.resize(image, target_shape)

def get_data_batch(image_paths, bounding_box_path, index, batch_size, crop_size):
      
      # Get a batch of images and their labels
      
      image_batch = []
      label_batch = []

      while len(image_batch) < batch_size and len(label_batch) < batch_size:

            try:
                  path = image_paths[index]
                  image = utils.get_image(path)

                  image_bounding_box = shapely.geometry.box(0, 0, image.shape[1], image.shape[0])
                  face_bounding_box = bounding_box_path(os.path.basename(path))

                  if geometry.bounding_box_iou(image_bounding_box, face_bounding_box) < 0.01:
                        raise InvalidBoundingBox("Invalid bounding box for image {}".format(path))
                  
                  scale = geometry.get_scale(image_bounding_box, crop_size)

                  scaled_image = get_scaled_image(image, scale)
                  scaled_bounding_box = geometry.get_scaled_bounding_box(face_bounding_box, scale)

                  # Randomly flip the image

                  if random.randint(0, 1) == 1:
                        scaled_image = cv2.flip(scaled_image, flipCode=1)

                        scaled_bounding_box = geometry.flip_bounding_box_y_axis(scaled_bounding_box, scaled_image.shape)

                  crops, labels = get_image_crop_labels(scaled_image, scaled_bounding_box, crop_size)

                  image_batch.extend(crops)
                  label_batch.extend(labels)

            #if image has an invalid bounding box, skip it and move on to the next image
            except (InvalidBoundingBox, CropException):
                  pass
      
            index += 1

            if index >= len(image_paths):
                  index = 0

      batch = list(zip(image_batch, label_batch))
      random.shuffle(batch)
      image_batch, label_batch = zip(*batch)

      return np.array(image_batch), np.array(label_batch)

def get_scaled_image(image, scale):
      
      # Scale the image so the resuling image is the same size as the integer sizes

      return cv2.resize(image, (round(scale * image.shape[1]), round(scale * image.shape[0])))

def get_image_crop_labels(image, bounding_box, crop_size):

      face_crop = get_random_face_crop(image, bounding_box, crop_size)

      non_face_crops = [
            get_random_non_face_crop(image, bounding_box, crop_size),
            get_random_face_part_crop(image, bounding_box, crop_size),
            get_random_small_scale_face_crop(image, bounding_box, crop_size)
      ]

      crops = [face_crop] + non_face_crops
      labels = [1, 0, 0, 0]

      return crops, labels

def get_random_face_crop(image, face_bounding_box, crop_size):

      bounds = face_bounding_box.bounds

      # try up to X times to get a valid crop

      for index in range(150):
            x = round(bounds[0] + random.randint(-crop_size, crop_size))
            y = round(bounds[1] + random.randint(-crop_size, crop_size))

            x_end = x + crop_size
            y_end = y + crop_size

            cropped_region = shapely.geometry.box(x, y, x_end, y_end)

            coordinates_valid = x >= 0 and y >= 0 and x_end < image.shape[1] and y_end < image.shape[0]

            is_iou_high  = geometry.bounding_box_iou(face_bounding_box, cropped_region) > 0.7

            if coordinates_valid and is_iou_high:
                  return image[y:y_end, x:x_end]

      # No valid crop found
      raise CropException("No valid face crop found")

def get_random_non_face_crop(image, face_bounding_box, crop_size):

      # try up to X times to get a valid crop

      for index in range(150):
            x = random.randint(0, image.shape[1] - crop_size)
            y = random.randint(0, image.shape[0] - crop_size)

            sampling_size = random.randint(10, min(image.shape[:2]))
            x_end = x + sampling_size
            y_end = y + sampling_size

            sampled_region = shapely.geometry.box(x, y, x_end, y_end)

            coordinates_valid = x >= 0 and y >= 0 and x_end < image.shape[1] and y_end < image.shape[0]

            is_iou_high  = geometry.bounding_box_iou(face_bounding_box, sampled_region) < 0.7

            if coordinates_valid and is_iou_high:
                  return image[y:y_end, x:x_end]

      # No valid crop found
      raise CropException("No valid face crop found")


def get_random_face_part_crop(image, face_bounding_box, crop_size):

      bounds = face_bounding_box.bounds

      # try up to X times to get a valid crop
      for index in range(150):

            face_width = int(bounds[2] - bounds[0])

            x = round(bounds[0] + random.randint(0, face_width))
            y = round(bounds[1] + random.randint(0, face_width))

            sampling_width = random.randint(face_width // 5, face_width)
            x_end = x + sampling_width
            y_end = y + sampling_width

            cropped_region = shapely.geometry.box(x, y, x_end, y_end)

            coordinates_valid = x >= 0 and y >= 0 and x_end < image.shape[1] and y_end < image.shape[0]

            is_iou_high  = geometry.bounding_box_iou(face_bounding_box, cropped_region) < 0.5

            if coordinates_valid and is_iou_high:
                  crop = image[y:y_end, x:x_end]
                  return cv2.resize(crop, (crop_size, crop_size))

      # No valid crop found
      raise CropException("No valid face crop found")

def get_random_small_scale_face_crop(image, face_bounding_box, crop_size):
      
            bounds = face_bounding_box.bounds
      
            # try up to X times to get a valid crop
            for index in range(150):
      
                  x = round(bounds[0] + random.randint(-2 * crop_size, 2 * crop_size))
                  y = round(bounds[1] + random.randint(-2 * crop_size, 2 * crop_size))
      
                  # Don't let x and y be negative
                  x = max(0, x)
                  y = max(0, y)

                  crop_width = 2 * crop_size \
                        if x + (2 * crop_size) < image.shape[1] and y + (2 * crop_size) < image.shape[0] \
                        else min(image.shape[1] - x - 1, image.shape[0] - y - 1)

                  x_end = x + crop_width
                  y_end = y + crop_width

                  cropped_region = shapely.geometry.box(x, y, x_end, y_end)
      
                  coordinates_valid = x >= 0 and x_end < image.shape[1] and \
                                y >= 0 and y_end < image.shape[0] and crop_width > crop_size
      
                  is_iou_high  = geometry.bounding_box_iou(face_bounding_box, cropped_region) < 0.5
      
                  if coordinates_valid and is_iou_high:
                        crop = image[y:y_end, x:x_end]
                        return cv2.resize(crop, (crop_size, crop_size))
      
            # No valid crop found
            raise CropException("No valid face crop found")

def get_smallest_expected_face_size(image_shape, min_face_size, min_face_size_to_image_ratio):
      image_ratio_based_size = round(min(image_shape[:2]) * min_face_size_to_image_ratio)
      return max(min_face_size, image_ratio_based_size)