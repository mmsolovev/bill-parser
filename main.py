import shutil

import pytesseract
from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello'}


@app.post('/image')
async def upload_image(image: UploadFile):
    with open("bill.jpg", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    pil_image = Image.open('bill.jpg')
    text = pytesseract.image_to_string(pil_image, lang='rus')
    print(text)
    return {'text': text}
