#wapp to use spacy

import spacy
nlp = spacy.load("en_core_web_lg")

doc = "kamal"

vdoc = nlp(doc)

print(vdoc)
print(vdoc.text)
print(vdoc.vector)
print(vdoc.vector.shape)


