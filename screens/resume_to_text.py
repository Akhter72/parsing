import os
import tempfile
import zipfile
import shutil
import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from helpers.get_text_from_file import getTextFromFile

def convert_to_text():
    st.title("Convert resume file to text")
    st.write("select folder to convert all resumes to .txt format")
    uploaded_files = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    if uploaded_files:
        zip_file, temp_dir = process_and_create_zip(uploaded_files)
        # Provide a download button for the zip file
        with open(zip_file, 'rb') as f:
            st.download_button(
                label="Download Converted Files as ZIP",
                data=f,
                file_name=zip_file,
                mime="application/zip"
            )
        # shutil.rmtree(temp_dir)  # Delete the temporary folder
        # os.remove(zip_file) 


def process_and_create_zip(uploaded_files):
    zip_filename = "converted_files.zip"
    
    # Create a temporary directory to store the converted text files
    temp_dir = tempfile.mkdtemp()

    # Loop through the uploaded files
    for uploaded_file in uploaded_files:
        # Get the extracted text
        text = getTextFromFile(uploaded_file)
        
        if text:
            # Save the extracted text as a .txt file
            text_filename = os.path.splitext(uploaded_file.name)[0] + ".txt"
            text_file_path = os.path.join(temp_dir, text_filename)
            with open(text_file_path, 'w') as f:
                f.write(text)

    # Create a zip file containing all the text files
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

    # Clean up the temporary directory
    shutil.rmtree(temp_dir)

    return zip_filename, temp_dir