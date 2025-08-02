# CV + SnowballStemmer

#import the lib
import pandas as pd 
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import SnowballStemmer

#load the data
data = pd.read_csv('sld2.csv')
print(data)

print()

ss = SnowballStemmer('english')

#text cleaning
def clean_data(txt):
    txt = txt.lower()
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = [t for t in txt if t not in stopwords.words('english')]
    txt = [ss.stem(t) for t in txt]
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