#import the lib
import pandas as pd 
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import PorterStemmer  

#load the data
data = pd.read_csv('kcfb1.csv')
print(data)

print()

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


data['clean_review'] = data['review'].apply(clean_data)
print(data['clean_review'])

#vectorize the data
cv = CountVectorizer()
vector = cv.fit_transform(data['clean_review'])
print(vector)

#features and target
features = pd.DataFrame(vector.toarray(), columns=cv.get_feature_names())
print(features)
target = data['label']

#model
model = MultinomialNB()
model.fit(features.values, target)

#predict
text = input("enter text ")
ctext = clean_data(text)
vtext = cv.transform([ctext])
print(vtext)
r1 = model.predict(vtext)
print(r1)

#internal
r2 = model.predict_proba(vtext)
print(r2)


