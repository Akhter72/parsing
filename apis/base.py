import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfFileReader, PdfReader
import docx

from llm.olama import parseResumeViaLlm

app = FastAPI(title="File Text Extractor API", description="API to extract text from PDF, DOCX, and TXT files", version="0.1.0")

def extract_text_from_docx(file_path):
    return extract_text_from_docx(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, "r") as f:
        return f.read()
    
def extract_text_from_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.post("/parse_resume")
async def extract_text(file: UploadFile = File(...)):
    file_path = os.path.join("temp", file.filename)
    os.makedirs("temp", exist_ok=True)
    
    with open(file_path, "wb") as f:
        f.write(await file.read())

    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        text = extract_text_from_docx(file_path)
    elif file_extension == ".txt":
        text = extract_text_from_txt(file_path)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    os.remove(file_path)

    json = parseResumeViaLlm(text)
    print(json)
    return JSONResponse(content= json, media_type="application/json")