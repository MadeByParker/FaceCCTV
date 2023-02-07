import tensorflow as tf
from tensorflow import keras

# build and train your face detection model
model = keras.Sequential([...])
model.compile(...)
model.fit(...)

# save the model
model.save("face_detection_model.h5")

# load the model in another Python script or program
loaded_model = keras.models.load_model("face_detection_model.h5")


