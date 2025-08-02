from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity

s1 = input("enter first string ")
s2 = input("enter second string ")

cv = CountVectorizer()
vector = cv.fit_transform([s1, s2])

res = pd.DataFrame(vector.toarray(), columns = cv.get_feature_names())
print(res)

cs = cosine_similarity(vector)
print(cs)

ans = cs[0,1]
print("similarity = ", round(ans * 100, 2), "%")

