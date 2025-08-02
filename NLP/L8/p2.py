#to find similarity between two text documents

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity

f1 = input("enter first file name ")
f = open(f1, "r")
s1 = f.read()
f.close()

f2 = input("enter second file name ")
f = open(f2, "r")
s2 = f.read()
f.close()

cv = CountVectorizer()
vector = cv.fit_transform([s1, s2])


res = pd.DataFrame(vector.toarray(), columns = cv.get_feature_names())
print(res)

cs = cosine_similarity(vector)
print(cs)

ans = cs[0,1]
print("similarity = ", round(ans * 100, 2), "%")

