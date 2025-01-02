import os
from PyPDF2 import PdfReader
import docx
import streamlit as st
import tempfile

def getTextFromFile(file):
    file_type = ""
    # temp_file_path = os.path.join("temp", file.name)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Write the uploaded file content to the temp file
        temp_file.write(file.getvalue())  # use getvalue() to access file content
        temp_file_path = temp_file.name
        print(temp_file_path)
        
    # Save uploaded file temporarily
    # with open(temp_file_path, "wb") as temp_file:
    #     temp_file.write(file.read())

    try:
    # Now process the file based on its type (PDF, DOCX, TXT)
        if file.type == "application/pdf":
            return extract_text_from_pdf(temp_file_path)
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return extract_text_from_docx(temp_file_path)
        elif file.type == "text/plain":
            return extract_text_from_txt(temp_file_path)
        else:
            return None
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

    return extracted_text

def getTextFromFilePath(file, file_extension):
    file_type = ""
    # temp_file_path = os.path.join("temp", file.name)
    # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    #     # Write the uploaded file content to the temp file
    #     temp_file.write(file.getvalue())  # use getvalue() to access file content
    #     temp_file_path = temp_file.name
    #     print(temp_file_path)
        
    # Save uploaded file temporarily
    # with open(temp_file_path, "wb") as temp_file:
    #     temp_file.write(file.read())

    try:
    # Now process the file based on its type (PDF, DOCX, TXT)
        if file_extension == "pdf":
            return extract_text_from_pdf(file)
        elif file_extension == "docx":
            return extract_text_from_docx(file)
        elif file_extension == ".txt":
            return extract_text_from_txt(file)
        else:
            return None
    finally:
        # Clean up the temporary file
        os.remove(file)

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

def save_text_format(file, file_type):
    text = getTextFromFile(file)
    output_file = f"output_{os.path.splitext(file)[0]}.txt"
    with open(output_file, 'w') as f:
        f.write(text)
    os.remove(f"temp_{file.name}")
    return output_file, text
