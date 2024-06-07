import streamlit as st
import csv
from docx import Document
import zipfile
from copy import deepcopy
from io import BytesIO

# Function to reset the session state
def reset_state():
    st.session_state.clear()

# Call the reset_state function at the start of the app
reset_state()

# Streamlit app
st.title("Auto Document Generator")

# Upload the template document
template_file = st.file_uploader("Upload Document Template (.docx)", type="docx")
if template_file:
    template_document = Document(template_file)

# Upload the CSV file
csv_file = st.file_uploader("Upload Data CSV (.csv)", type="csv")
if csv_file:
    data = list(csv.DictReader(csv_file))

# Input for unique file name prefix
unique_name = st.text_input("Enter a unique name for the generated files:")

# Dropdown for document type selection
document_type = st.selectbox(
    "Select the type of document:",
    ["Award Letter", "Grant Agreement", "Commitment Letter", "Other"]
)

# Function to replace placeholders in the document
def replace_placeholders(document, data):
    for key, value in data.items():
        # Replace placeholders in the paragraphs
        for paragraph in document.paragraphs:
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)
        # Replace placeholders in the header
        for section in document.sections:
            header = section.header
            for paragraph in header.paragraphs:
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key, value)

# Generate documents and create a zip file
if st.button("Generate Documents") and template_file and csv_file and unique_name:
    document_paths = []
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for row in data:
            # Create a new document based on the template
            new_document = deepcopy(template_document)

            # Replace placeholders with data from the current row
            replace_placeholders(new_document, row)

            # Define the file path for the new document and change name
            file_name = f"{unique_name}_{row['grantee_name']}_{row['lea_name']}_{row['aoi']}_{document_type.replace(' ', '')}.docx"
            doc_buffer = BytesIO()
            new_document.save(doc_buffer)
            doc_buffer.seek(0)

            # Add the document to the zip file
            zipf.writestr(file_name, doc_buffer.read())

    zip_buffer.seek(0)
    st.download_button(
        label="Download Documents",
        data=zip_buffer,
        file_name="documents.zip",
        mime="application/zip"
    )
