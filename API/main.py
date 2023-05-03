from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io
from keras.models import load_model
import uvicorn
import deepai
import requests

app = FastAPI()

model = load_model('./models/facecctv.h5', compile=False)
# Load face detection model
face_model = cv2.CascadeClassifier('./models/facecctv.xml')

    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route. Please use the /docs route to access the API documentation. Or go to Github Repository for more information. URL: https://github.com/Parker06/FaceCCTV"}

# first 'static' specify route path, second 'static' specify html files directory.
app.mount('/api', StaticFiles(directory='showcase',html=True))

# Define an API endpoint to handle image uploads
@app.post("/task/full-image-examination")
async def DetectFacesAndImproveQualityImage(file: UploadFile = File(...)):
    contents = await file.read()

    # Convert the byte stream into a numpy array
    nparr = np.frombuffer(contents, np.uint8)

    # Read the numpy array as an image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw bounding boxes on the image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Apply a bilateral filter to reduce noise while preserving edges
    bilateral_img = cv2.bilateralFilter(img, 9, 75, 75)

    # Convert the enhanced image back to bytes
    enhanced_img_bytes = cv2.imencode(".jpg", bilateral_img)[1].tobytes()

    # Return the enhanced image as a StreamingResponse
    return StreamingResponse(io.BytesIO(enhanced_img_bytes), media_type="image/jpeg", headers={'Content-Disposition': 'attachment; filename=result.jpg'})

# Define an API endpoint to handle image uploads
@app.post("/task/face-detection")
async def DetectFacesInImage(file: UploadFile = File(...)):
    contents = await file.read()

    # Convert the byte stream into a numpy array
    nparr = np.frombuffer(contents, np.uint8)

    # Read the numpy array as an image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw bounding boxes on the image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Convert image to bytes for streaming response
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()
    
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/jpeg")

@app.post("/task/image-enhancement")
async def EnhanceImageQuality(file: UploadFile = File(...)):
# Read the uploaded image file as a byte stream
    contents = await file.read()

    '''# Convert the byte stream into a numpy array
    nparr = np.frombuffer(contents, np.uint8)

    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        data={
            'image': nparr,
        },
        headers={'api-key': 'ed913ed8-f985-4246-ac90-1ad55e5cf072'}
    )
    colorized_image_bytes = r.content

    # Return the enhanced image as a StreamingResponse
    return StreamingResponse(io.BytesIO(colorized_image_bytes), media_type="image/jpeg", headers={'Content-Disposition': 'attachment; filename=colorized.jpg'})'''

    # Convert the byte stream into a numpy array
    nparr = np.frombuffer(contents, np.uint8)

    # Read the numpy array as an image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the CLAHE (Contrast Limited Adaptive Histogram Equalization) algorithm to enhance the contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_img = clahe.apply(gray)

    # Apply a bilateral filter to reduce noise while preserving edges
    bilateral_img = cv2.bilateralFilter(clahe_img, 9, 75, 75)

    # Convert the enhanced image back to bytes
    enhanced_img_bytes = cv2.imencode(".jpg", bilateral_img)[1].tobytes()

    # Return the enhanced image as a StreamingResponse
    return StreamingResponse(io.BytesIO(enhanced_img_bytes), media_type="image/jpeg", headers={'Content-Disposition': 'attachment; filename=enhanced.jpg'})

# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)