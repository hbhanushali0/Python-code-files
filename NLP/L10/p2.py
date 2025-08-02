#wapp to find similarity between two sentences

import spacy

nlp = spacy.load("en_core_web_lg")

s1 = input(" enter first sentence ")
vs1 = nlp(s1)

s2 = input(" enter second sentence ")
vs2 = nlp(s2)

simi = vs1.similarity(vs2)
print(round(simi * 100, 2), "%")



