import pdfplumber

# Path to the PDF file
pdf_path = "D:\\Python\\LINK OF THE LINK.pdf"

# Initialize a list to store table data
table_data = []
text_data=""

# Extract tables from the PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()  # Extract the entire table as a list of rows
        text = page.extract_text()
        if table:
            table_data.append(table)
        if text:
            text_data+= text
textsplit= text_data.split("\n")
# Assuming the table_data contains one table (adjust indexing as needed)
table = table_data[0]

# Assuming the table has headers in the first row
headers = table[0]

# Generate sentences based on the table data
sentences = []
for row in table[1:]:
    sentence = f"{headers[0]} is {row[0]}, {headers[1]} is {row[1]}, and {headers[2]} is {row[2]}."
    sentences.append(sentence)

sentences.append(text_data)

# Print the generated sentences
for sentence in sentences:
    print(sentence)