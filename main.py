from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from typing import List
from archivos import s3

app = FastAPI()

@app.post("/file/")
def upload_file(file: UploadFile = File(...)):
    s3.Bucket('libramanage').put_object(Key=file.filename, Body=file.file)