#wapp to do text cleaning using spacy
import spacy
nlp = spacy.load('en_core_web_lg')

data = input("enter some sentence ")

def clean_data(txt):
    txt = txt.lower()
    txt = nlp(txt)
    txt = [t for t in txt]
    txt = [t for t in txt if not t.is_punct]
    txt = [t for t in txt if not t.is_stop]
    txt = [t.lemma_ for t in txt]
    return txt 

cdata = clean_data(data)
print("data ", data)
print("clean data ", cdata)