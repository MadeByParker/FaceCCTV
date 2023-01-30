import os 

import shapely.geometry
import cv2
import numpy as np
import tqdm

import sys
 
# adding Folder_2 to the system path
sys.path.append('../../face/')

import face.config as config
import face.utils as utils
import face.models as models
import face.detections as detect
import face.geometry as geometry

def detect_face_correctly(image, face_bounding_box, cascade_classifier):
      # Makes sure that the cascade classifier detects the face correctly

      # using the cascade classifier calls the multi scale function which makes the detections
      detections = cascade_classifier.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

      # if there isnt a face in the image then return false

      # else draw a bounding box around each face using the x and y coordinates of the top left corner and the width and height of the face
      if len(detections) != 1:
          return False
      else:
            left, top, width, height = detections[0]
            detection_bounding_box = shapely.geometry.box(left, top, left + width, top + height)

            detection_correct = geometry.bounding_box_iou(face_bounding_box, detection_bounding_box) > 0.5

            return detection_correct

def check_accuracy(image_path, bounding_box_map):
      # checks the accuracy of the face detection


      detection_scores = []


      filters_path = os.path.expanduser("~/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")
      cascade_classifier = cv2.CascadeClassifier(filters_path)

      
      for path in tqdm.tqdm(image_path):
            image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

            image_bounding_box = shapely.geometry.box(0, 0, image.shape[1], image.shape[0])
            face_bounding_box = bounding_box_map[os.path.basename(path)]

            # Only try to search for faces if they are larger than 1% of image. If they are smaller,
            # ground truth bounding box is probably incorrect
            if geometry.bounding_box_iou(image_bounding_box, face_bounding_box) > 0.01:

                  value = 1 if detect_face_correctly(image, face_bounding_box, cascade_classifier) else 0
                  detection_scores.append(value)

      print("Detection accuracy: {:.2f}%".format(np.mean(detection_scores) * 100))


def model_detect_face_correctly(image, face_bounding_box, model, configuration):
      #checks to make sure the model detects the face correctly

      detections = detect.FaceCCTVModel(image, model, configuration).get_face_detection()

      # if there isnt a face in the image then return false

      # else draw a bounding box around each face using the x and y coordinates of the top left corner and the width and height of the face
      if len(detections) != 1:
            return False
      else:
            is_detection_correct = geometry.bounding_box_iou(face_bounding_box, detections[0].bounding_box) > 0.5

            return is_detection_correct

def check_model_accuracy(image_path, bounding_box_map, filepath=None):
      # checks the accuracy of the VGG16 model

      detection_scores = []

      model = models.get_vgg_model(config.image_shape)
      model.load_weights(config.model_path)


      for path in tqdm.tqdm(image_path):
            image = utils.get_image(path)

            image_bounding_box = shapely.geometry.box(0, 0, image.shape[1], image.shape[0])
            face_bounding_box = bounding_box_map[os.path.basename(path)]

            # Only try to search for faces if they are larger than 1% of image. If they are smaller,
            # ground truth bounding box is probably incorrect
            if geometry.bounding_box_iou(image_bounding_box, face_bounding_box) > 0.01:

                  value = 1 if model_detect_face_correctly(image, face_bounding_box, model, config) else 0
                  detection_scores.append(value)

                  if filepath is not None:
                        with open(filepath, mode='a') as file:
                              file.write("{}\n".format(np.mean(detection_scores)))

      print("Model accuracy: {:.2f}%".format(np.mean(detection_scores) * 100))

def main():

      # dataset = "custom_dataset"
      dataset= "wider_face_dataset"

      dataset_path = os.path.join(config.dataset_path, dataset)

      image_path_file = utils.join(dataset_path, "training_images.txt")
      bounding_box_file = utils.join(dataset_path, "training_bounding_boxes.txt")

      image_paths = [path.strip() for path in utils.get_file_lines(image_path_file)]
      bounding_box_map = geometry.get_bounding_box_map(bounding_box_file)

      #check accuracy
      check_model_accuracy(image_paths, bounding_box_map, filepath="/logs/model_accuracy_log.txt")

if __name__ == "__main__":
      main()