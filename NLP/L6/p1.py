#n-grams
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 

text = ["food was not good but staff was courteous"]

cv = CountVectorizer(ngram_range=(2,2))
vector = cv.fit_transform(text)
print(vector)

features = pd.DataFrame(vector.toarray(), columns = cv.get_feature_names())
print(features)

#unigram        (1,1)
#bigram         (2,2)
#trigram        (3,3)
#uni + bi       (1,2)
#bi + tri       (2,3)
#uni + bi + tri (1,3)



