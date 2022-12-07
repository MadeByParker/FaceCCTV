from schema import Face

def get_detected_faces(face: Face):
    if not (face.face_detected):
        return 'No face detected in image'
    else:
        return 'Face detected in image'