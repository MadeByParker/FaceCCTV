## Bring in dependencies

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class image(BaseModel):
    def __init__(self, image):
        self.image = image

@app.get("/")

async def image_endpoint():
    return {"message": "Hello World"}


@app.post("/files/")
async def create_file(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(description="A file read as UploadFile"),
):
    return {"filename": file.filename}