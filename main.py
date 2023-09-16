import spacy
import csv
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ''
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text

# Load the custom NER model you trained
nlp = spacy.load("custom_ner_nav_model_new")

#text = extract_text_from_pdf("C:\\Users\\EldoRoopa\\Downloads\\UPDATED_NLP_COURSE\\UPDATED_NLP_COURSE\\00-Python-Text-Basics\\Business_Proposal.pdf")
#text = extract_text_from_pdf("D:\\Python\\testcase1.pdf")
text = "ROR for the bank is 56 . Bank of Pensylvania has performed very well in 2023. The testing was in progress and we decided to add more strings. \n the NAV is 74."

# Process text with the custom NER model
doc = nlp(text)

ner = nlp.get_pipe("ner")
print(ner.labels)


# Initialize data for the table
table_data = [["COMPANY", "NAV", "ROR"]]

# Initialize variables to temporarily store information
current_company = None
current_nav = None
current_ror = None

for ent in doc.ents:
    print(ent.text, ent.label_)


# Process each token in the document
for ent in doc.ents:
    if ent.label_ == "COMPANY":
        current_company = ent.text.lower()
    elif ent.label_ == "NAV":
        current_nav = ent.text
    elif ent.label_ == "ROR":
        current_ror = ent.text

    # If we have gathered all information, append to table_data
    if current_company and current_nav and current_ror:
        table_data.append([current_company, current_nav, current_ror])
        current_company = None
        current_nav = None
        current_ror = None

# Write data to CSV
csv_path = "nav_ror.csv"
with open(csv_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(table_data)

print("CSV file generated successfully.")
