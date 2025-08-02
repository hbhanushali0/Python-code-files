import spacy
from spacytextblob.spacytextblob import SpacyTextBlob 
import pandas as pd 

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("spacytextblob")

data = pd.read_csv("hr1_ap24.csv")
print(data)

def gs(txt):
    txt = nlp(txt)
    score = txt._.polarity
    if score > 0.0:
        return "pos"
    elif score < 0.0:
        return "neg"
    else:
        return "neu"

data['sentiment'] = data['review'].apply(gs)
print(data)

data.to_csv("hrr.csv")
