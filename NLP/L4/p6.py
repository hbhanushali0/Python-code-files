#import lib
import pandas as pd 
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from pickle import *

#load the data
data = pd.read_csv('spam_ap24.csv')
print(data)

#check for null
print(data.isnull().sum())

ps = PorterStemmer()
#text cleaning
def clean_data(txt):
    txt = txt.lower()
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = [t for t in txt if t not in stopwords.words('english')]
    txt = [ps.stem(t) for t in txt]
    txt = " ".join(txt)
    return txt

data['clean_message'] = data['Message'].apply(clean_data)
print(data['clean_message'])

#text vectorizer
tv = TfidfVectorizer()
tvector = tv.fit_transform(data['clean_message'])

#feature and target
features = pd.DataFrame(tvector.toarray(), columns = tv.get_feature_names())
print(features)
target = data['Category']
print(target)

#train and test
x_train, x_test, y_train, y_test = train_test_split(features, target)

#model
model = MultinomialNB()
model.fit(x_train,y_train)



#save the model and save the vector
f = open('vector.pkl', 'wb')
dump(tv,f)
f.close()

f = open('model.pkl', 'wb')
dump(model,f)
f.close()