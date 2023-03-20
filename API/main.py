from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from keras.models import load_model

app = FastAPI()

model = load_model('model.h5')
    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route."}

# Define a function to detect faces in an image
def detect_faces(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resized = tf.image.resize(rgb, (240, 240))

    faces = model.predict(np.expand_dims(resized/255,0))
    # Create a copy of the original image
    #image_copy = np.array(image)
    # Draw bounding boxes around the faces
    #for face in faces:
        #x, y, w, h = face
        #cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # interpret the prediction
    if faces[0] > 0.8:
            # Create a copy of the original image
        image_copy = np.array(image)
        # Draw bounding boxes around the faces
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)
    else:
        return False


# Define an API endpoint to handle image uploads
@app.post("/task/full-image-examination")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Load the image from memory
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # Detect faces in the image
    result_image = detect_faces(image)
    # enhance the image
    if result_image != False:
        byte_io = io.BytesIO()
        result_image.save(byte_io, 'JPEG')
        byte_io.seek(0)
        return StreamingResponse(byte_io, media_type='image/jpeg', headers={'Content0-Disposition': 'attachment; filename=result.jpg'})
    else:
        return {"message": "No face detected"}


# Define an API endpoint to handle image uploads
@app.post("/task/face-detection")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Load the image from memory
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # Detect faces in the image
    result_image = detect_faces(image)
    if result_image != False:
        byte_io = io.BytesIO()
        result_image.save(byte_io, 'JPEG')
        byte_io.seek(0)
        return StreamingResponse(byte_io, media_type='image/jpeg', headers={'Content0-Disposition': 'attachment; filename=result.jpg'})
    else:
        return {"message": "No face detected"}

# Define an API endpoint to handle image uploads
@app.post("/task/image-enhancement")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Load the image from memory
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # enhance the image
    result_image = enhance_image(image)
    if result_image != False:
        byte_io = io.BytesIO()
        result_image.save(byte_io, 'JPEG')
        byte_io.seek(0)
        return StreamingResponse(byte_io, media_type='image/jpeg', headers={'Content0-Disposition': 'attachment; filename=result.jpg'})
    else:
        return {"message": "No image uploaded"}

# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)