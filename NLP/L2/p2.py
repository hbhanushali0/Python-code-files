#import lib
import pandas as pd 
from nltk import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option('display.max_colwidth',1000)

#load the data
data = pd.read_csv('data2.csv')
print(data)

print()

#text cleaning


def clean_data(txt):
    txt = txt.lower()
    txt = txt.replace("'", " ")
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = [t for t in txt if t not in stopwords.words('english')]
    txt = " ".join(txt)
    return txt

data['clean_review'] = data['review'].apply(clean_data)
print(data['clean_review'])

#text Vecotrization
cv = CountVectorizer()
vector = cv.fit_transform(data['clean_review'])

features = pd.DataFrame(vector.toarray(), columns=cv.get_feature_names())
print(features)

