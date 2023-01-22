from mtcnn import MTCNN
import face_recognition
import cv2

# initialise the detector class.
detector = MTCNN()

# load an image as an array
image = face_recognition.load_image_file("./1.jpg")

# detect faces from input image.
face_locations = detector.detect_faces(image)

# draw bounding box and five facial landmarks of detected face
for face in zip(face_locations):
    (x, y, w, h) = face[0]['box']
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()