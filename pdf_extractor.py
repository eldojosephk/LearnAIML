from fastapi import FastAPI, UploadFile, File, HTTPException
import re
import csv
import PyPDF2
import spacy

app = FastAPI()

# Load the custom NER model you trained
nlp = spacy.load("custom_ner_nav_model_new")


@app.post("/extract")
async def extract_entities_from_pdf(pdf_file: UploadFile):
    try:
        # Read the uploaded PDF file
        pdf_text = extract_text_from_pdf(pdf_file.file)

        # Process text with the custom NER model
        doc = nlp(pdf_text)

        # Initialize data for the table
        table_data = [["COMPANY", "NAV", "ROR"]]

        # Initialize variables to temporarily store information
        current_company = None
        current_nav = None
        current_ror = None

        for ent in doc.ents:
            if ent.label_ == "COMPANY":
                current_company = ent.text.lower()
            elif ent.label_ == "NAV":
                current_nav = ent.text
            elif ent.label_ == "ROR":
                current_ror = ent.text

            # If we have gathered all information, append to table_data
            if current_company and current_nav and current_ror:
                table_data.append({"COMPANY": current_company, "NAV": current_nav, "ROR": current_ror})
                current_company = None
                current_nav = None
                current_ror = None

        # Write data to CSV
        csv_path = "nav_ror.csv"
        with open(csv_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(table_data)
        response_data = {
            "message": "CSV file generated successfully.",
            "data": table_data[1:],  # Exclude header row
        }
        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def extract_text_from_pdf(pdf_file):
    text = ''
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text
