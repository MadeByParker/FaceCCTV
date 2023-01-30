import random


import face.detections as detect
import face.processing as processing
import face.utils as utils


def get_data_batch(image_paths, bounding_box_path, index, batch_size, crop_size):

      if batch_size % 4 != 0:
            raise ValueError("Batch size must be divisible by 4")

      images_per_batch = batch_size // 4

      paths = [path.strip() for path in utils.get_file_lines(image_paths)]
      random.shuffle(paths)

      bounding_boxes = utils.get_bounding_boxes(bounding_box_path)

      index = 0

      while True:

            batch = processing.get_batch(paths, bounding_boxes, index, images_per_batch, crop_size)
            yield(batch)

            if index + images_per_batch < len(paths):
                  index += images_per_batch

            else:
                  index = 0
                  random.shuffle(paths)