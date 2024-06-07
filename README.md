# Auto Document Generator

This Streamlit application generates documents from a template and CSV data. The user can upload a `.docx` template and a CSV file containing the data. The application will replace placeholders in the template with data from the CSV and generate new documents. The generated documents can be downloaded as a ZIP file.

## Features

- Upload a `.docx` template
- Upload a CSV file with data
- Replace placeholders in the template with data from the CSV
- Generate documents based on the user's selection of document type (Award Letter, Grant Agreement, Commitment Letter, Other)
- Download the generated documents as a ZIP file

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/auto-document-generator.git
    cd auto-document-generator
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to use the app.

3. Upload your `.docx` template and CSV file.

4. Enter a unique name for the generated files.

5. Select the type of document you want to generate.

6. Click the "Generate Documents" button to create the documents and download the ZIP file.

## Requirements

- Python 3.6 or higher
- `streamlit`
- `python-docx`

You can install the required packages using the provided `requirements.txt` file.

## Example CSV Format

Your CSV file should have the following format:

```csv
grantee_name,grant_number,grantee_street,grantee_citystatezip,award_amount_numerical,convert_numbers_to_words,contact_name,contact_title,contact_number,contact_email,sig_name,sig_title
Example Grantee,12345,123 Example St,Example City, ST 12345,1000,One Thousand,Jane Doe,Director,555-1234,jane.doe@example.com,John Smith,CEO
Another Grantee,67890,456 Another St,Another City, ST 67890,2000,Two Thousand,John Roe,Manager,555-5678,john.roe@example.com,Jane Smith,CFO
