#cv + tt

import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

data = pd.read_csv('mr_ap24.csv')
print(data)

print()

cv = CountVectorizer()
vector = cv.fit_transform(data['review'])
#print(vector)
#print(cv.vocabulary_)
tt = TfidfTransformer()
tvector = tt.fit_transform(vector)

features = pd.DataFrame(tvector.toarray(), columns = cv.get_feature_names())
print(features)

