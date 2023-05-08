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
face_model = cv2.CascadeClassifier('./models/facecctv.xml')

    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route. Please use the /docs route to access the API documentation. Or go to Github Repository for more information. URL: https://github.com/Parker06/FaceCCTV"}

@app.get("/status")
async def status():
    return {"status": "API is running"}

@app.post("/task/full-image-examination")
async def DetectFacesAndImproveQualityImage(file: UploadFile = File(...)):
    contents = await file.read()

    # Convert the byte stream into a numpy array
    nparr = np.frombuffer(contents, np.uint8)

    # Read the numpy array as an image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    prototxt = "./models/colorization_deploy_v2.prototxt"
    model = "./models/colorization_release_v2.caffemodel"
    points = "./models/pts_in_hull.npy"
    
    net = cv2.dnn.readNetFromCaffe(prototxt, model)  # Load model
    pts = np.load(points)  # Load cluster
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    
    # Convert image from BGR to grayscale and back to RGB
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    
    # Scaling (normalizing) the image by dividing everything by 255
    scaled = image.astype("float32") / 255.0
    
    lab = cv2.cvtColor(scaled, cv2.COLOR_RGB2LAB)  # Convert RGB to LAB
    resized = cv2.resize(lab, (224, 224))
    
    L = cv2.split(resized)[0]  # Extract L value
    L -= 50
    
    # Set input as L to get predicted a and b
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))  # Find a and b
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))  # Resize again after prediction to original
    
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)  # Concatenate the a and b values to the image
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)  # Convert LAB to BGR (since OpenCV works in BGR not RGB)
    colorized = np.clip(colorized, 0, 1)  # Limit values in the numpy array (image)
    colorized = (255 * colorized).astype("uint8")  # Changing pixel intensity back to 255
    
    # Detect faces in the original image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw bounding boxes on the enhanced image
    for (x, y, w, h) in faces:
        cv2.rectangle(colorized, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    _, encoded_img = cv2.imencode('.jpg', colorized)
    
    # Return the enhanced image with bounding boxes as a StreamingResponse
    return StreamingResponse(io.BytesIO(encoded_img.tobytes()), media_type="image/jpeg", headers={'Content-Disposition': 'attachment; filename=result.jpg'})


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
    
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/jpeg", headers={'Content-Disposition': 'attachment; filename=detected.jpg'})

@app.post("/task/image-enhancement")
async def EnhanceImageQuality(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    prototxt = "./models/colorization_deploy_v2.prototxt"
    model = "./models/colorization_release_v2.caffemodel"
    points = "./models/pts_in_hull.npy"
    
    net = cv2.dnn.readNetFromCaffe(prototxt, model)  # Load model
    pts = np.load(points)  # Load cluster
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    
    # Convert image from BGR to grayscale and back to RGB
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    
    # Scaling (normalizing) the image by dividing everything by 255
    scaled = image.astype("float32") / 255.0
    
    lab = cv2.cvtColor(scaled, cv2.COLOR_RGB2LAB)  # Convert RGB to LAB
    resized = cv2.resize(lab, (224, 224))
    
    L = cv2.split(resized)[0]  # Extract L value
    L -= 50
    
    # Set input as L to get predicted a and b
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))  # Find a and b
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))  # Resize again after prediction to original
    
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)  # Concatenate the a and b values to the image
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)  # Convert LAB to BGR (since OpenCV works in BGR not RGB)
    colorized = np.clip(colorized, 0, 1)  # Limit values in the numpy array (image)
    colorized = (255 * colorized).astype("uint8")  # Changing pixel intensity back to 255
    
    _, encoded_img = cv2.imencode('.jpg', colorized)
    
    # Return the enhanced image as a StreamingResponse
    return StreamingResponse(io.BytesIO(encoded_img.tobytes()), media_type="image/jpeg", headers={'Content-Disposition': 'attachment; filename=enhanced.jpg'})

# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)