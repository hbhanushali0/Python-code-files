import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("spacytextblob")

data = input("enter some sentence ")

vdata = nlp(data)
score = vdata._.subjectivity
if score > 0.5:
    print("subjective")
else:
    print("objective")
    