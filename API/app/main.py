from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn
import numpy as np
import cv2
from PIL import Image
import io
import tensorflow as tf
from mangum import Mangum

from app.api.api_v1.api import router as api_router

app = FastAPI()
    
@app.get("/")
async def root():
    return {"message": "Hello and Welcome to the Face Detection API, this is the default route."}

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)


# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
