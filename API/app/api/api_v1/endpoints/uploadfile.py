from fastapi import File, UploadFile, APIRouter
from fastapi.responses import FileResponse
import uvicorn
import numpy as np
import cv2
from PIL import Image
import io
import tensorflow as tf
from tensorflow.keras.models import load_model

router = APIRouter()

# Load the face detection model
model_path = "./API/models/facecctv.h5"
model = load_model(model_path)

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

    sample_coords = [1][0]
    global message
    message = {"num_faces": len(faces[0])}
    # interpret the prediction
    if faces[0] > 0.8:
        # Controls the main rectangle
        cv2.rectangle(image, 
                      tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                      tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                            (255,0,0), 2)
        # Controls the label rectangle
        cv2.rectangle(image, 
                      tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int), 
                                    [0,-30])),
                      tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                    [80,0])), 
                            (255,0,0), -1)
        
        # Controls the text rendered
        cv2.putText(image, 'face', tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                               [0,-5])),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        return True
    else:
            return False


# Define an API endpoint to handle image uploads
@router.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Load the image from memory
    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    # Detect faces in the image
    is_face_detected = detect_faces(image)
    mess = message
    # Convert the output image to JPEG format and save it to memory
    #image_file = io.BytesIO()
    #Image.fromarray(output_image).save(image_file, "JPEG")
    #image_file.seek(0)
    # Return the output image as a response
    #return FileResponse(image_file, media_type="image/jpeg")
    if is_face_detected:
        
        return {"message": "Face detected " + str(mess)}
    else:
        return {"message": "No face detected"}

