#cv

import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv('mr_ap24.csv')
print(data)

print()

cv = CountVectorizer()
vector = cv.fit_transform(data['review'])
print(vector)
print(cv.vocabulary_)

features = pd.DataFrame(vector.toarray(), columns = cv.get_feature_names())
print(features)

