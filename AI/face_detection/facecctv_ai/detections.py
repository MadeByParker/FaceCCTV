# Face Detection using Deep Learning Model

import shapely.geometry
import numpy as np
import cv2

import sys
sys.path.append('../')

import facecctv_ai.utils as utils
import facecctv_ai.geometry as geometry
import facecctv_ai.processing as processing

class FaceCandidateDetermined:
      # Determine what is a face candidate to be detected

      def __init__(self, crop_coordinates, cropped_image, focus_coordinates):
            self.crop_coordinates = crop_coordinates
            self.cropped_image = cropped_image
            self.focus_coordinates = focus_coordinates

class FaceDetection:
      def __init__(self, bounding_box, accuracy_score):
            self.bounding_box = bounding_box
            self.accuracy_score = accuracy_score

      def __eq__(self, other):
            # Equality comparison to compare objects to determine if they are the same then return a boolean value

            if not isinstance(other, self.__class__):
                  return False

            return self.bounding_box.equals(other.bounding_box) and self.accuracy_score == other.accuracy_score

      def _get_scaled(self, scale):
            # Get the scaled bounding box

            rescaled_bounding_box = geometry.scale_bounding_box(self.bounding_box, scale)
            return FaceDetection(rescaled_bounding_box, self.accuracy_score)

def get_faces_generator(image, crop_size, stride, batch_size):
      # Returns a generator that generates batches of images, that is cropped by the value of crop_size. Stride is the number of betweeen each images which is cropped. Batch_size is the number of images that is cropped at a time.


      if crop_size < stride:
            raise ValueError("Crop size ({}) must be greater than or equal to stride size ({})".format(crop_size, stride))

      face_candidates = []

      offset = (crop_size - stride) // 2

      y = 0

      while y + crop_size <= image.shape[0]:
            x = 0

            while x + crop_size <= image.shape[1]:

                  crop_coordinates = shapely.geometry.box(x, y, x + crop_size, y + crop_size)
                  cropped_image = image[y:y + crop_size, x:x + crop_size]

                  focus_coordinates = shapely.geometry.box(x + offset, y + offset, x + crop_size - offset, y + crop_size - offset)

                  face_candidate = FaceCandidateDetermined(crop_coordinates, cropped_image, focus_coordinates)
                  face_candidates.append(face_candidate)

                  if len(face_candidates) == batch_size:
                        yield face_candidates
                        face_candidates = []

                  x += stride

            y += stride

      #if final batch is not empty then yield it else return nothing

      if len(face_candidates) > 0:
            yield face_candidates
      else:
            return

class SingleScaleHeatmap:
      #this computes the heatmap for a single scale image given the face prescence, model and parameters

      def __init__(self, image, model, configuration):
            self.image = image
            self.model = model
            self.configuration = configuration
      
      def get_heatmap(self):
            # returns a heatmap for the image

            heatmap = np.zeros(self.image.shape[:2], dtype=np.float32)

            face_candidates_generator = get_faces_generator(self.image, self.configuration.crop_size, self.configuration.stride, self.configuration.batch_size)

            for face_candidates in face_candidates_generator:

                  accuracy_scores = self._get_candidate_accuracy_scores(face_candidates)

                  for face_candidate, accuracy_score in zip(face_candidates, accuracy_scores):

                        x_start, y_start, x_end, y_end = [round(value) for value in face_candidate.focus_coordinates.bounds]
                        heatmap[y_start:y_end, x_start:x_end] = accuracy_score

            return heatmap

      def _get_candidate_accuracy_scores(self, face_candidates):
            # returns the accuracy scores for the face candidates

            face_crops = [face_candidate.cropped_image for face_candidate in face_candidates]
            accuracy_scores = self.model.predict(np.array(face_crops), batch_size=self.configuration.batch_size)

            return accuracy_scores

class HeatmapGenerator:

      def __init__(self, image, model, configuration):
            self.image = image
            self.model = model
            self.configuration = configuration

      def get_heatmap(self):
            # returns a heatmap for the image

            heatmap = np.zeros(self.image.shape[:2], dtype=np.float32)

            image = self._get_largest_scale_image()

            while min(image.shape[:2]) > self.configuration.crop_size:

                  image = processing.get_scaled_image(image, self.configuration.image_scaling_ratio)

                  single_scale_heatmap = SingleScaleHeatmap(image, self.model, self.configuration).get_heatmap()

                  rescaled_single_scale_heatmap = cv2.resize(single_scale_heatmap, (heatmap.shape[1], heatmap.shape[0]))

                  heatmap = np.maximum(heatmap, rescaled_single_scale_heatmap)

            return heatmap

      def _get_largest_scale_image(self):
            # returns the image with the largest scale

            smallest_face_size = processing.get_smallest_face_size(image_shape=self.image.shape, min_face_size=self.configuration.min_face_size, min_face_size_to_image_ratio=self.configuration.min_face_size_to_image_ratio)

            scale = self.configuration.crop_size / smallest_face_size

            return processing.get_scaled_image(self.image, scale)

class ComplexDetection:
      # class to detect faces in an image that are not easy (e.g. faces that are not frontal)

      @staticmethod
      def non_maximum_suppression(detections, iou_threshold):
            # returns the detections after non maximum suppression

            complex_detections = []

            for detection in detections:

                  unique_id = 0
                  similar_detection_found = False

                  while unique_id < len(complex_detections) and similar_detection_found is False:
                        complex_detection = complex_detections[unique_id]

                        if geometry.bounding_box_iou(detection.bounding_box, complex_detection.bounding_box) > iou_threshold:
                              complex_detections[unique_id] = complex_detection \
                                    if complex_detection.accuracy_score < detection.accuracy_score else detection

                              similar_detection_found = True

                        unique_id += 1

                  if similar_detection_found is False:
                        complex_detections.append(detection)

            return complex_detections

      @staticmethod
      def average_scores(face_detections, iou_threshold):
            # returns the detections after averaging the scores

            face_group_list = []

            for face_detection in face_detections:

                  group_found = False

                  group_id = 0

                  while group_id < len(face_group_list) and group_found is False:
                        current_group = face_group_list[group_id]
                        member_id = 0

                        while member_id < len(current_group) and group_found is False:

                              group_member = current_group[member_id]

                              if geometry.bounding_box_iou(face_detection.bounding_box, group_member.bounding_box) > iou_threshold:

                                    current_group.append(face_detection)
                                    group_found = True
                              
                              member_id += 1

                        group_id += 1

                  if group_found is False:
                        group = [face_detection]
                        face_group_list.append(group)

            complex_detections = []

            #average for each group
            for group in face_group_list:

                  coordinates = np.array([detection.bounding_box for detection in group])
                  average_coordinates = np.mean(coordinates, axis=0)

                  int_coordinates = [round(coordinate) for coordinate in average_coordinates]

                  accuracy_score = max([detection.accuracy_score for detection in group])

                  average_detection = FaceDetection(shapely.geometry.box(*int_coordinates), accuracy_score)
                  complex_detections.append(average_detection)

            return complex_detections

class SingleScaleFaceDetection:
      # class to detect faces in a single scale image

      def __init__(self, image, model, configuration):
            self.image = image
            self.model = model
            self.configuration = configuration

      def get_face_detections(self):
            # returns face detections found in an image under the given configuration

            face_detections = []

            face_candidates_generator = get_faces_generator(self.image, self.configuration.crop_size, self.configuration.stride, self.configuration.batch_size)

            for face_candidates in face_candidates_generator:

                  accuracy_scores = self._get_candidate_accuracy_scores(face_candidates)
                  face_detections.extend(self._get_positive_face_detections(face_candidates, accuracy_scores))

            return ComplexDetection.average_scores(face_detections, iou_threshold=0.2)

      def _get_candidate_accuracy_scores(self, face_candidates):
            # returns the accuracy scores for the face candidates

            face_crops = [face_candidate.cropped_image for face_candidate in face_candidates]
            accuracy_scores = self.model.predict(np.array(face_crops), batch_size=self.configuration.batch_size)

            return accuracy_scores

      def _get_positive_face_detections(self, face_candidates, accuracy_scores):
            # returns the face detections with accuracy scores above the threshold

            face_detections = []

            for face_candidate, accuracy_score in zip(face_candidates, accuracy_scores):

                  if accuracy_score > 0.9:
                        detection = FaceDetection(face_candidate.bounding_box, accuracy_score)
                        face_detections.append(detection)

            return face_detections

class FaceDetector:
      # class to detect faces in an image. They are searched with numerous configurations

      def __init__(self, image, model, configuration):

            self.input_image_scale = 1 if min(image.shape[:2]) < 500 else 500 / min(image.shape[:2])

            self.image = processing.get_scaled_image(image, self.input_image_scale)
            self.model = model
            self.configuration = configuration

      def get_face_detections(self):
            # returns the face detections in the image

            current_image_scale = self._get_largest_scale()
            image = processing.get_scaled_image(self.image, current_image_scale)

            face_detections = []

            while min(image.shape[:2]) > self.configuration.crop_size:

                  current_image_scale_detections = SingleScaleFaceDetection(image, self.model, self.configuration).get_face_detections()

                  rescaled_detections = [face_detections.get_scaled(1 / current_image_scale) for face_detections in current_image_scale_detections]
                  face_detections.extend(rescaled_detections)

                  current_image_scale *= self.configuration.image_rescale_ratio
                  image = processing.get_scaled_image(self.image, current_image_scale)

            complex_detections = ComplexDetection.average_scores(face_detections, iou_threshold=0.2)
            return [face_detection.get_scaled(1 / self.input_image_scale) for face_detection in complex_detections]

      def _get_largest_scale(self):
            smallest_face_size = processing.get_smallest_face_size(image_shape=self.image.shape, min_face_size=self.configuration.min_face_size, min_face_size_to_image_ratio=self.configuration.min_face_size_to_image_ratio)

            return self.configuration.crop_size / smallest_face_size
                        
