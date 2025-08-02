#import lib
import pandas as pd 
from nltk import word_tokenize
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from pickle import *

#load the data
data = pd.read_csv("new_reviews.tsv", sep="\t")
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


data['clean_review'] = data['Review'].apply(clean_data)
print(data['clean_review'])


#model and vector creation
f = open("rr_model.pkl", "rb")
model = load(f)
f.close()

f = open("rr_vector.pkl", "rb")
cv = load(f)
f.close()


#predict
x_data = cv.transform(data['clean_review']).toarray()
y_pred = model.predict(x_data)
data['mclass'] = y_pred.tolist()
print(data['mclass'])

data.to_csv('f2.csv')