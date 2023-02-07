import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

# load the saved model
model = keras.models.load_model("face_detection_model.h5")

# load an image into memory
image = cv2.imread("example_image.jpg")

# preprocess the image
input_image = cv2.resize(image, (224, 224))
input_image = np.expand_dims(input_image, axis=0)
input_image = input_image / 255.

# make a prediction on the image
prediction = model.predict(input_image)

# interpret the prediction
if prediction[0][0] > 0.5:
    print("Face detected")
else:
    print("No face detected")
