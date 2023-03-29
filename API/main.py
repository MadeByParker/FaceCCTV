from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import io
import tensorflow as tf
from keras.models import load_model
import uvicorn

app = FastAPI()

model = load_model('./models/facecctv.h5')
    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route. Please use the /docs route to access the API documentation. Or go to Github Repository for more information. URL: https://github.com/Parker06/FaceCCTV"}

# first 'static' specify route path, second 'static' specify html files directory.
app.mount('/api', StaticFiles(directory='showcase',html=True))


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
        # Convert the image to bytes
        image_bytes = io.BytesIO()
        return Image.fromarray(image_copy) 
    else:
        return False
    



# Define an API endpoint to handle image uploads
@app.post("/task/full-image-examination")
async def full_image_examination(file: UploadFile = File(...)):
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
async def detect(file: UploadFile = File(...)):
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
async def enhance(file: UploadFile = File(...)):
    contents = await file.read()
    # Load the image from memory
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # enhance the image
    enhancer = ImageEnhance.Sharpness(Image)
    enhanced_img = enhancer.enhance(2.0)

    # Convert the enhanced image to bytes
    enhanced_img_bytes = io.BytesIO()
    enhanced_img.save(enhanced_img_bytes, format='JPEG')
    enhanced_img_bytes.seek(0)
    if enhanced_img != False:
        byte_io = io.BytesIO()
        enhanced_img.save(byte_io, 'JPEG')
        byte_io.seek(0)
        return StreamingResponse(byte_io, media_type='image/jpeg', headers={'Content0-Disposition': 'attachment; filename=result.jpg'})
    else:
        return {"message": "No image uploaded"}

# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)