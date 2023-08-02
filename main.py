import pytesseract
from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello'}


@app.post('/image')
async def upload_image(image: UploadFile):
    text = pytesseract.image_to_string(image, lang='rus')
    print(text)
    return {'text': text}
