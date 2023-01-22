import os 
import logging

import cv2

def get_file_lines(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def get_file_lines_count(file_path):
      return len(get_file_lines(file_path))

def get_logger(file_path):
      os.makedirs(os.path.dirname(file_path), exist_ok=True)
      logger = logging.getLogger("FaceCCTV")
      file_handler = logging.FileHandler(file_path, mode="w")
      logger.setLevel(logging.INFO)
      logger.addHandler(file_handler)

      return logger

def get_image(image_path):
      return cv2.imread(image_path) / 255
