import nltk
from nltk import word_tokenize

#eg1 
data = "kamal sir rocks"
print(data)

r1 = word_tokenize(data)
print(r1)

#eg2
data = "kamal Sir! rocks."
r2 = word_tokenize(data)
print(r2)

from string import punctuation
r3 = [r for r in r2 if r not in punctuation]
print(r3)

