import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Load SpaCy English tokenizer
nlp = spacy.load("en_core_web_sm")

# Path to the extracted text file
file_path = "knowledge_base.text"

# Ensure file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Use SpaCy to split into sentences
doc = nlp(text)
sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

# Save to CSV
df = pd.DataFrame(sentences, columns=["sentence"])
df.to_csv("knowledge_sentences.csv", index=False)

print("Knowledge base saved to knowledge_sentences.csv using SpaCy")
