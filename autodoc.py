import streamlit as st
import csv
from docx import Document
import zipfile
from copy import deepcopy
from io import BytesIO
import re

# ... (previous code remains the same)

# Function to replace placeholders in the document
def replace_placeholders(document, data):
  for paragraph in document.paragraphs:
      for key, value in data.items():
          placeholder = f"{{{key}}}"
          if placeholder in paragraph.text:
              paragraph.text = paragraph.text.replace(placeholder, str(value))

  for section in document.sections:
      for part in (section.header, section.footer):
          for paragraph in part.paragraphs:
              for key, value in data.items():
                  placeholder = f"{{{key}}}"
                  if placeholder in paragraph.text:
                      paragraph.text = paragraph.text.replace(placeholder, str(value))

  for table in document.tables:
      for row in table.rows:
          for cell in row.cells:
              for paragraph in cell.paragraphs:
                  for key, value in data.items():
                      placeholder = f"{{{key}}}"
                      if placeholder in paragraph.text:
                          paragraph.text = paragraph.text.replace(placeholder, str(value))

# ... (rest of the code remains the same)
