FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update && apt-get -y install tesseract-ocr
RUN apt-get update && apt-get -y install libtesseract-dev
RUN apt-get update && apt-get -y install tesseract-ocr-rus
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]