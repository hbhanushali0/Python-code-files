#import lib
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from string import punctuation
from nltk import word_tokenize
from nltk.corpus import stopwords


#load the data
data=pd.read_csv('movie_review_1.csv')
print(data)

print()

#check or null
print(data.isnull().sum())


#text cleaning
def clean_data(txt):
    txt = txt.lower()
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = [t for t in txt if t not in stopwords.words('english')]
    txt = " ".join(txt)
    return txt


data['clean_review'] = data['review'].apply(clean_data)
print(data['clean_review'])

#text vectorization
cv = CountVectorizer()
vector = cv.fit_transform(data['clean_review'])
print(vector)

#feature and target
features = pd.DataFrame(vector.toarray(), columns=cv.get_feature_names())
print(features)
target = data['result']
print(target)

#model
model = MultinomialNB()
model.fit(features.values,target)

#predict
review = input("enter review ")
nreview = clean_data(review)
creview = cv.transform([nreview])
res = model.predict(creview)
print(res)

#internal
ans = model.predict_proba(creview)
print(ans)
nans = ans.ravel().tolist()
pn = round(nans[0] * 100, 2)
pp = round(nans[1] * 100, 2)

print("negative ", pn, "%", sep="")
print("positive ", pp, "%", sep="")

