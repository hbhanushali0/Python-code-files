#import lib
import pandas as pd 
from nltk import word_tokenize
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from pickle import *

#load the data
data = pd.read_csv("news_test.csv")
print(data)
print(data.info())

#check for null data
print(data.isnull().sum())

#text cleaning
def clean_data(txt):
    txt = txt.replace(" ' ", " ")
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = " ".join(txt)
    return txt


data['clean_text'] = data['text'].apply(clean_data)
print(data['clean_text'])


#model and vector restoration
f = open("fn_model.pkl", "rb")
model = load(f)
f.close()

f = open("fn_vector.pkl", "rb")
cv = load(f)
f.close()

#predict
x_data = cv.transform(data["clean_text"]).toarray()
y_pred = model.predict(x_data)
data["mclass"] = y_pred.tolist()
print(data["mclass"])

data.to_csv('f1.csv')

cr = classification_report(data['mclass'], data['label'])
print(cr)

cr = classification_report(data['label'], data['mclass'])
print(cr)



