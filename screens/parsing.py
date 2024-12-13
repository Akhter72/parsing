import streamlit as st
from helpers.get_text_from_file import getTextFromFile
from data_extraction import processText

def parsing_screen():
    st.title("Resume Parsing")

    st.markdown("Upload a file (PDF, DOCX, or TXT), and we will extract the text for further processing.")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        with st.spinner("Processing the file..."):
            extracted_text = getTextFromFile(uploaded_file)

        if extracted_text:
            st.success("File processed successfully!")

            st.text_area("Extracted Text", processText(extracted_text), height=300)

            # Placeholder for additional text processing logic
            st.markdown("### Processed Output")
            processed_output = extracted_text.lower()  # Example: convert text to lowercase
            st.text_area("Processed Text", processed_output, height=300)
        