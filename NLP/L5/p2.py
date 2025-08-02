#import lib
import pandas as pd 
from nltk import word_tokenize
from string import punctuation
from pickle import load



#text cleaning
def clean_data(txt):
    txt = txt.lower()
    txt = txt.replace('"', " ")
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = " ".join(txt)
    return txt


#restore the model and vector
f = open("lang_detection_model.pkl", "rb")
model = load(f)
f.close()

f = open("lang_detection_vector.pkl", "rb")
tv = load(f)
f.close()


#prediction
text = input("enter text ")
clean_text = clean_data(text)
vtext = tv.transform([clean_text])
ans = model.predict(vtext)
print(ans[0])

