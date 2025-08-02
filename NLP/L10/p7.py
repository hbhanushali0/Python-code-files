import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("spacytextblob")

data = input("enter some sentence ")

vdata = nlp(data)
score = vdata._.polarity
print(score)


if score > 0.0:
    print("pos")
elif score < 0.0:
    print("neg")
else:
    print("neu")

    