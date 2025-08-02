#import lib
import pandas as pd 
from nltk import word_tokenize
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from pickle import dump

#load the data
data = pd.read_csv('langdet_ap24.csv')
print(data)

print()

#check for null data
print(data.isnull().sum())

#text cleaning
def clean_data(txt):
    txt = txt.lower()
    txt = txt.replace('"', " ")
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = " ".join(txt)
    return txt

data['clean_text'] = data['Text'].apply(clean_data)
print(data['clean_text'])

#text vecotrizer
tv = TfidfVectorizer()
vector = tv.fit_transform(data['clean_text'])

#features and target
features = pd.DataFrame(vector.toarray(), columns=tv.get_feature_names())
print(features.value)
target = data["Language"]

#train and test
x_train , x_test, y_train, y_test = train_test_split(features, target)

#model
model = MultinomialNB()
model.fit(x_train, y_train)

#classification report
cr = classification_report(y_test, model.predict(x_test))
print(cr)

#save the model and vector
f = open("lang_detection_model,pkl", "wb")
dump(model,f)
f.close()

f = open("lang_detection_vector.pkl", "wb")
dump(tv,f)
f.close()


