import os
from PyPDF2 import PdfReader
import docx
import streamlit as st

def getTextFromFile(file):
    file_type = file.name.split('.')[-1].lower()
    temp_file_path = os.path.join("temp", file.name)

    # Save uploaded file temporarily
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(file.read())

    try:
        if file_type == "pdf":
            extracted_text = extract_text_from_pdf(temp_file_path)
        elif file_type == "docx":
            extracted_text = extract_text_from_docx(temp_file_path)
        elif file_type == "txt":
            extracted_text = extract_text_from_txt(temp_file_path)
        else:
            st.error("Unsupported file format. Please upload a PDF, DOCX, or TXT file.")
            return None
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

    return extracted_text

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from a DOCX file
def extract_text_from_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to extract text from a TXT file
def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text