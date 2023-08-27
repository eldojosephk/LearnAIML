import spacy
import random
import json
from spacy.training.example import Example  # Import the Example class

# Load a pre-trained model
nlp = spacy.load("en_core_web_sm")

# Load your annotated data
with open("annotated_game_data.json", "r") as f:
    annotated_data = json.load(f)

# Add entity annotations to the model's pipeline
ner = nlp.get_pipe("ner")

# Add labels to the NER
for _, annotations in annotated_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable other pipeline components during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

# Train only NER component
with nlp.disable_pipes(*other_pipes):
    n_iter = 50
    for _ in range(n_iter):
        random.shuffle(annotated_data)
        losses = {}
        for text, annotations in annotated_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)  # Create an Example instance
            nlp.update([example], drop=0.5, losses=losses)
        print(losses)

# Save the trained model
nlp.to_disk("custom_ner_game_model")
