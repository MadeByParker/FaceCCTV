import os 
import random

import vlogging
import numpy as np
import tqdm
import tqdm

from ..facecctv_ai import config
from ..facecctv_ai import utils
from ..facecctv_ai import models
from ..facecctv_ai import detections as detect
from ..facecctv_ai import geometry
from ..facecctv_ai import processing
from ..facecctv_ai import data_generator

def log_data_batch(data_generator, logger):

      for index in range(8):

            images, labels = next(data_generator)

            images = [image * 255 for image in images]
            images = [processing.scale_image(image, 100) for image in images]
            logger.info(vlogging.VisualRecord("image batch", images, str(labels)))

def log_crop_prediction(data_generator, logger):

      model = models.get_vgg_model(config.image_shape)
      model.load_weights(config.model_path)

      for index in range(8):

            images, labels = next(data_generator)
            predictions = model.predict(images)

            images = [image * 255 for image in images]
            images = [processing.scale_image(image, 100) for image in images]

            logger.info(vlogging.VisualRecord("image batch", images, str(predictions)))

def log_heatmaps(image_path_file, logger):

      model = models.get_vgg_model(config.image_shape)
      model.load_weights(config.model_path)

      paths = [path.strip() for path in utils.get_file_lines(image_path_file)]
      random.shuffle(paths)

      for path in tqdm.tqdm(paths[:10]):

            image = utils.get_image(path)

            

            heatmap = detect.Heatmap(image, model, config.face_search_config).get_heatmap()

            scaled_images = [255 * image, 255 * heatmap]
            scaled_images = [processing.scale_image(image, 200) for image in scaled_images]

            logger.info(vlogging.VisualRecord("image heatmap", scaled_images, str(image.shape)))

def log_face_detections(image_path_file, logger):

      model = models.get_vgg_model(config.image_shape)
      model.load_weights(config.model_path)

      paths = [path.strip() for path in utils.get_file_lines(image_path_file)]
      random.shuffle(paths)

      for path in tqdm.tqdm(paths[:10]):

            image = utils.get_image(path)

            detections = detect.FaceDetection(image, model, config.face_search_config).get_face_detection()

            for face_detection in detections:
                  geometry.draw_bounding_box(image, face_detection.bounding_box, color=(0, 255, 0), thickness=3)

            logger.info(vlogging.VisualRecord("image detections", image * 255, "{} - {}".format(path, str(image.shape))))

def main():

      logger = utils.get_logger(config.get_log_path)

      #dataset = "custom_dataset"
      dataset = "wider_face_dataset"

      dataset_path = os.path.join(config.dataset_path, dataset)

      image_path_file = utils.join(dataset_path, "training_images.txt")
      bounding_box_file = utils.join(dataset_path, "training_bounding_boxes.txt")

      generator = data_generator.get_data_generator(image_path_file, bounding_box_file, batch_size=8, crop_size=config.crop_size)

      log_face_detections(image_path_file, logger)

if __name__ == "__main__":
      main()