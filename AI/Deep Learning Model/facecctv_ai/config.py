# Config File

# Path to the folder containing the images
dataset_path = "../data/test/"

# Log path
log_path = "../logs/log.txt"

batch_size = 64

crop_size = 64

image_shape = (crop_size, crop_size, 3)

stride = 8

class FaceDetectionConfig():
      def __init__(self, crop_size, stride, batch_size):
            self.crop_size = crop_size
            self.stride = stride
            self.batch_size = batch_size

face_search_config = FaceDetectionConfig(crop_size, stride, batch_size)

min_face_size = 5

min_face_to_image_ratio = 0.05

image_rescale_ratio = 0.9

class FaceDetection(FaceDetectionConfig):
      def __init__(self, crop_size, stride, batch_size, min_face_size, min_face_to_image_ratio, image_rescale_ratio):
            
            super().__init__(crop_size, stride, batch_size)
            self.min_face_size = min_face_size
            self.min_face_to_image_ratio = min_face_to_image_ratio
            self.image_rescale_ratio = image_rescale_ratio

face_detection_config = FaceDetection(crop_size=crop_size, stride=stride, batch_size=batch_size, min_face_size=min_face_size, min_face_to_image_ratio=min_face_to_image_ratio, image_rescale_ratio=image_rescale_ratio)

model_path = "../models/facecctv_model.h5"