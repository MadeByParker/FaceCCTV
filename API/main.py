from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io
import tensorflow as tf
from keras.models import load_model
import uvicorn

app = FastAPI()

model = load_model('./models/facecctv.h5', compile=False)
    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route. Please use the /docs route to access the API documentation. Or go to Github Repository for more information. URL: https://github.com/Parker06/FaceCCTV"}

# first 'static' specify route path, second 'static' specify html files directory.
app.mount('/api', StaticFiles(directory='showcase',html=True))

# Define a function to detect faces in an image
def detect_faces(image):
    # Convert the image to RGB format
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Resize the image to 300x300 pixels (the input size required by the SSD model)
    resized_image = cv2.resize(rgb_image, (300, 300))
    # Convert the image to a format that can be processed by the SSD model
    input_data = np.expand_dims(resized_image, axis=0)
    # Run the SSD model on the input data to detect faces
    predictions = model.predict(input_data)
    # Extract the bounding boxes and confidence scores from the predictions
    boxes = predictions[0, :, :4]
    scores = predictions[0, :, 4:]
    # Select the bounding boxes with a confidence score above a threshold (e.g. 0.5)
    threshold = 0.8
    selected_boxes = boxes[scores > threshold]
    
    # Draw bounding boxes around the selected faces
    if len(selected_boxes) > 0:
        for box in selected_boxes:
            x1, y1, x2, y2 = box
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    else:
        # If no face is detected, return None
        return None
    # Return the image with bounding boxes around the detected faces
    return image


# Define an API endpoint to handle image uploads
@app.post("/task/full-image-examination")
async def full_image_examination(file: UploadFile = File(...)):
# Read the image from the uploaded file
    contents = await file.read()
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # Detect faces in the image
    result_image = detect_faces(image)
    if result_image is not None:
        img = Image.fromarray(result_image)

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
        return StreamingResponse(io.BytesIO(result_image_bytes), media_type='image/jpeg')
    else:
        # If no face is detected, return an error message
        return {"message": "No face detected in the uploaded image."}


# Define an API endpoint to handle image uploads
@app.post("/task/face-detection")
async def detect(file: UploadFile = File(...)):
# Read the image from the uploaded file
    contents = await file.read()
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # Detect faces in the image
    result_image = detect_faces(image)
    if result_image is not None:
        # Convert the result image to bytes and return it as a response
        result_image_bytes = cv2.imencode('.jpg', result_image)[1].tobytes()
        return StreamingResponse(io.BytesIO(result_image_bytes), media_type='image/jpeg')
    else:
        # If no face is detected, return an error message
        return {"message": "No face detected in the uploaded image."}

# Define an API endpoint to handle image uploads
@app.post("/task/image-enhancement")
async def enhance(file: UploadFile = File(...)):
    contents = await file.read()
    # Load the image from memory
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    img = Image.fromarray(image)

    # Unblur the image using ImageFilter.UnsharpMask
    unblurred_img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    # Convert to RGB color mode if not already in that mode
    if unblurred_img.mode != 'RGB':
        unblurred_img = unblurred_img.convert('RGB')
    # Improve the image quality using ImageEnhance.Sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(unblurred_img)
    enhanced_img = sharpness_enhancer.enhance(2)

    # Convert the enhanced image to bytes
    enhanced_img_bytes = io.BytesIO()
    enhanced_img.save(enhanced_img_bytes, format='JPEG')
    enhanced_img_bytes.seek(0)

    return StreamingResponse(enhanced_img_bytes, media_type='image/jpeg', headers={'Content-Disposition': 'attachment; filename=result.jpg'})


# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)