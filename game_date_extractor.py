import spacy
import csv

# Load the custom NER model you trained
nlp = spacy.load("custom_ner_game_model")

# Input text
text = "Basketball is Ryan's favorite game in 2023. he spends 1 hour playing that. He earned 7 billion"

# Process text with the custom NER model
doc = nlp(text)

ner = nlp.get_pipe("ner")
print(ner.labels)


# Initialize data for the table
table_data = [["GAME", "HOURS", "INCOME"]]

# Initialize variables to temporarily store information
current_company = None
current_nav = None
current_ror = None

for ent in doc.ents:
    print(ent.text, ent.label_)


# Process each token in the document
for ent in doc.ents:
    if ent.label_ == "GAME":
        current_company = ent.text.lower()
    elif ent.label_ == "HOURS":
        current_nav = ent.text
    elif ent.label_ == "INCOME":
        current_ror = ent.text

    # If we have gathered all information, append to table_data
    if current_company and current_nav and current_ror:
        table_data.append([current_company, current_nav, current_ror])
        current_company = None
        current_nav = None
        current_ror = None

# Write data to CSV
csv_path = "game_data.csv"
with open(csv_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(table_data)

print("CSV file generated successfully.")
