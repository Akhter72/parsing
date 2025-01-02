import streamlit as st
from helpers.get_text_from_file import getTextFromFile
from llm.olama import parseResumeViaLlm

def parsing_screen_llm():
    st.title("Ollama Resume Parsing")

    st.markdown("Upload a file (PDF, DOCX, or TXT), and we will extract the text for further processing.")

    # uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

    uploaded_files = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    if uploaded_files:
        with open('validation.txt', 'w') as f:

            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    with st.spinner("Processing the file..."):
                        extracted_text = getTextFromFile(uploaded_file)

                    if extracted_text:
                        
                        st.success("File processed successfully!")

                        response = parseResumeViaLlm(extracted_text)
                        f.write(f'Resume: \n {extracted_text}\n\n JSON Response:\n{response}\n\n')
                        st.text_area("Extracted Text", response, height=300)

                        # Placeholder for additional text processing logic
                        st.markdown("### Processed Output")
                        processed_output = extracted_text.lower()  # Example: convert text to lowercase
                        st.text_area("Processed Text", processed_output, height=300)
        f.close()