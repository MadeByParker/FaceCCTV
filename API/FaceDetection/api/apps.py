import os
from django.apps import AppConfig
from django.conf import settings
from tensorflow import keras
from keras.models import load_model


class FaceDetectionModel(AppConfig):
    name = 'facecctvAPI'
    MODEL_FILE = os.path.join(settings.MODELS, "facecctv.h5")
    model = keras.models.load_model(MODEL_FILE)
