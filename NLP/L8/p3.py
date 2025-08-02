#to find similarity between two pdf's
#pip install PyMuPDF
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import fitz

f1 = input("enter firsst file name ")
d1 = fitz.open(f1)
s1 = ""
for d in d1:
    s1 = s1 + d.get_text()

f2 = input(" enter second file name ")
d2 = fitz.open(f2)
s2 = ""
for d in d2:
    s2 = s2 + d.get_text()

cv = CountVectorizer()
vector = cv.fit_transform([s1, s2])

res = pd.DataFrame(vector.toarray(), columns = cv.get_feature_names())
print(res)

cs = cosine_similarity(vector)
print(cs)

ans = cs[0,1]
print("similarity = ", round(ans * 100, 2), "%")