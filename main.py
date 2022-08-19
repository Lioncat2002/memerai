import os

import torchvision.transforms as transforms
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from pydantic import BaseModel
import generate_caption

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageData(BaseModel):
    data: str


@app.get("/")
def read_root():
    return {"This is": "a test"}


@app.post("/image/")
async def imageupload(data: UploadFile = File(...)):

    # checking if the uplaoded file is image or not
    if not data.filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
        return {"error": "File is not an image"}

    f = data.file
    # Temporary code to write image to drive
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    with open("tmp/image.jpg", "wb") as fs:
        fs.write(f.read())
    f = Image.open(f)
    caption=generate_caption.generate(f)
    return {"got": {"top": caption}}
