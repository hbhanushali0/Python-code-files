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
data = pd.read_csv("news_train.csv")
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

#text vectorization
cv = CountVectorizer(ngram_range=(2,2))
vector = cv.fit_transform(data['clean_text'])

#features and target
features = pd.DataFrame(vector.toarray(), columns = cv.get_feature_names())
target = data['label']

#train and test
x_train, x_test, y_train, y_test = train_test_split(features, target)

#model
model = MultinomialNB()
model.fit(x_train,y_train)

#performance
cr = classification_report(y_test, model.predict(x_test))
print(cr)

#model and vector creation
f = open("fn_model.pkl", "wb")
dump(model, f)
f.close()

f = open("fn_vector.pkl", "wb")
dump(cv, f)
f.close()

