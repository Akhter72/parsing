import streamlit as st
from screens.parsing import parsing_screen
from screens.resume_to_text import convert_to_text

# Sidebar for navigation
screen = st.sidebar.selectbox("Select a Screen", ("Parsing", "Convert to Text"))

# Render the selected screen
if screen == "Parsing":
    parsing_screen()
elif screen == "Convert to Text":
    convert_to_text()
