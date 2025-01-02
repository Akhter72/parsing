import streamlit as st
from screens.parsing import parsing_screen
from screens.resume_to_text import convert_to_text
from screens.ollama_parsing import parsing_screen_llm

# Sidebar for navigation
screen = st.sidebar.selectbox("Select a Screen", ("Parsing", "Convert to Text", "Parsing via LLM"))

# Render the selected screen
if screen == "Parsing":
    parsing_screen()
elif screen == "Convert to Text":
    convert_to_text()
elif screen == "Parsing via LLM":
    parsing_screen_llm()