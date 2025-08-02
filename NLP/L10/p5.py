#removing punctuations and stopwords
import spacy
nlp = spacy.load("en_core_web_lg")

data = input("senter some sentence ")
data = data.lower()

vdata = nlp(data)
tokens = [v for v in vdata]
print(tokens)

pdata = [t for t in tokens if not t.is_punct]
print(pdata)

sdata = [p for p in pdata if not p.is_stop]
print(sdata)

