from pydantic import BaseModel

class Face(BaseModel):
    face_detected: bool = False