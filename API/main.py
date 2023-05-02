from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io
from keras.models import load_model
import uvicorn

app = FastAPI()

model = load_model('./models/facecctv.h5', compile=False)
# Load face detection model
face_cascade = cv2.CascadeClassifier('./models/facecctv.xml')

    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route. Please use the /docs route to access the API documentation. Or go to Github Repository for more information. URL: https://github.com/Parker06/FaceCCTV"}

# first 'static' specify route path, second 'static' specify html files directory.
app.mount('/api', StaticFiles(directory='showcase',html=True))

# Define an API endpoint to handle image uploads
@app.post("/task/full-image-examination")
async def DetectFacesAndImproveQualityImage(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw bounding boxes on the image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        
    # Convert image to bytes for streaming response
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()

    # Return image with bounding boxes as a downloadable response

    # Unblur the image using ImageFilter.UnsharpMask
    unblurred_img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    # Convert to RGB color mode if not already in that mode
    if unblurred_img.mode != 'RGB':
        unblurred_img = unblurred_img.convert('RGB')
    # Improve the image quality using ImageEnhance.Sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(unblurred_img)
    enhanced_img = sharpness_enhancer.enhance(2)

    # Convert the result image to bytes and return it as a response
    result_image_bytes = cv2.imencode('.jpg', enhanced_img)[1].tobytes()
    return StreamingResponse(io.BytesIO(result_image_bytes), media_type='image/jpeg', headers={'Content-Disposition': 'attachment; filename=improved_image.jpg'})


# Define an API endpoint to handle image uploads
@app.post("/task/face-detection")
async def DetectFacesInImage(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw bounding boxes on the image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Convert image to bytes for streaming response
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()
    
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/jpeg")

# Define an API endpoint to handle image uploads
@app.post("/task/image-enhancement")
async def EnhanceImageQuality(file: UploadFile = File(...)):
# Load the image from memory using Pillow
    image = Image.open(io.BytesIO(file))

    # Convert to RGB color mode if not already in that mode
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Unblur the image using ImageFilter.UnsharpMask
    unblurred_img = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # Improve the image quality using ImageEnhance.Sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(unblurred_img)
    enhanced_img = sharpness_enhancer.enhance(2)

    # Convert the colorized image to bytes
    enhanced_img_bytes = io.BytesIO()
    enhanced_img.save(enhanced_img_bytes, format='JPEG')
    enhanced_img_bytes.seek(0)

    return StreamingResponse(enhanced_img_bytes, media_type='image/jpeg', headers={'Content-Disposition': 'attachment; filename=colorized.jpg'})


# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)