#tokenization using spacy
import spacy
nlp = spacy.load("en_core_web_lg")

data = input("enter some sentence ")
data = data.lower()
vdata = nlp(data)
tokens = [v for v in vdata]

print(tokens)

