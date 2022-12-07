from io import BytesIO
import numpy as np
import tensorflow as tf
from keras.applications.imagenet_utils import decode_predictions
from keras.models import load_model
from PIL import Image

model = None

def load_AI_model():
    model = load_model('../../model/facecctv.h5')
    print("Model loaded")
    return model

def predict(image: Image.Image):
    global model
    if model is None:
        model = load_AI_model()

    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0

    result = decode_predictions(model.predict(image), 2)[0]

    response = []
    for  i, res in enumerate(result):
        resp = {}
        resp['label'] = res[1]
        resp["loss"] = f"{res[2]*100:.2f}%"
        response.append(resp)
    
    return response

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image