from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse
from typing import List
from archivos import upload_file
import requests

app = FastAPI()

@app.post("/file/")
async def upload_files(file: UploadFile = File(...)):
    url_archivo_subido = await upload_file(file)
    return {"url": url_archivo_subido}
    