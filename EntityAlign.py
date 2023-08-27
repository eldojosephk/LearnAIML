import spacy
from spacy.training import offsets_to_biluo_tags

# Load a pre-trained model
nlp = spacy.load("en_core_web_sm")

text = "Bank of Pensilvania has performed very well in 2023. Nav for the bank is 13.2 and the ROR is 17."
entities = [(0, 19, 'COMPANY'), (73, 77, 'NAV'), (93, 95, 'ROR')]
tags = offsets_to_biluo_tags(nlp.make_doc(text), entities)
print(tags)
