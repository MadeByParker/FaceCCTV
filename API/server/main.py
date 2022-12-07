from fastapi import FastAPI, UploadFile, File
import uvicorn
from starlette.responses import RedirectResponse

from API.components import predict, read_imagefile
from API.schema import Face
from API.components.prediction import face_detection_check

app_desc = """<h2>Try this app by uploading any image with `upload/`</h2>
<h2>FaceCCTV API</h2>
<br>by Harry Parker"""

app=FastAPI(title='FaceCCTV AI Model API', description=app_desc)   


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="https://github.com/Parker06/FaceCCTV/tree/main/API")

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())

    prediction = predict(image)

    return prediction

@app.post("/api/face-detection-check")
def check_risk(face: Face):
    return face_detection_check.get_detected_faces(face)


if __name__ == "__api__":
    uvicorn.run(app, debug=True)