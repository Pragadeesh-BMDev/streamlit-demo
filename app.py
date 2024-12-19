import glob
import os
import re

import pandas as pd
import streamlit as st
import gettext as _
from PIL import Image

import base64

st.set_page_config(layout="wide")


# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
# with col2:
#     st.markdown(("# 30 Days of Streamlit"))


# Sidebar
st.sidebar.header(("About"))

# Display content

# Path to the PDF file
pdf_path = "highlighted_example1.pdf"

# Read the PDF file as binary
with open(pdf_path,"rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)

# Display the PDF in an iframe
st.markdown(
    f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" 
    width="100%" height="1000rem" style="border: none;"></iframe>
    """,
    unsafe_allow_html=True,
)

#---------------------------------------------------------------------------------------------------------                -------

# import streamlit as st
# import base64

# # Sample JSON data for the right pane
# sample_json = {
#     "Title": "Sample PDF",
#     "Author": "John Doe",
#     "Summary": "This is a brief summary of the document.",
#     "Keywords": ["Streamlit", "PDF", "UI", "Example"]
# }

# # Creating two columns
# col1, col2 = st.columns([1, 1])

# # Left column: PDF Viewer
# # with col1:
# # Path to the PDF file
# pdf_path = "highlighted_example1.pdf"

# # Read the PDF file as binary
# with open(pdf_path, "rb") as pdf_file:
#     pdf_data = pdf_file.read()

# # Encode the binary PDF data to base64 for rendering
# base64_pdf = base64.b64encode(pdf_data).decode("utf-8")

# # Display the PDF in an iframe
# st.markdown(
#     f"""
#     <iframe src="data:application/pdf;base64,{base64_pdf}" 
#     width="100%" height="100%" style="border: none;"></iframe>
#     """,
#     unsafe_allow_html=True,
# )
#     # st.header("PDF Viewer")
#     # uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    
#     # if uploaded_file:
#     #     # Using pdfplumber to extract and display PDF content
#     #     with pdfplumber.open('highlighted_example.pdf') as pdf:
#     #         st.subheader("Pages Preview")
#     #         for page_number, page in enumerate(pdf.pages):
#     #             st.write(f"Page {page_number + 1}")
#     #             st.text(page.extract_text())

#     #         # Optional: Provide the entire document for download
#     #         full_text = "\n".join([page.extract_text() for page in pdf.pages])
#     #         st.download_button("Download Extracted Text", full_text)

# # Right column: JSON Information
# # with col2:
# #     st.header("Summary & Info")
# #     st.subheader("JSON Data")
# #     st.json(sample_json)
