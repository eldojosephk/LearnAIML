import spacy
from spacy.training import offsets_to_biluo_tags

# Load a pre-trained model
nlp = spacy.load("en_core_web_sm")

text = "There we so many years before the home and  the testing was not upto date. Bank of Scotland has performed very well in 2023. ROR for the bank is 19 . The testing was in progress and we decided to add more strings.the NAV is 74."
entities = [(75, 91, 'COMPANY'), (224, 226, 'NAV'), (145, 147, 'ROR')]
tags = offsets_to_biluo_tags(nlp.make_doc(text), entities)
print(tags)
