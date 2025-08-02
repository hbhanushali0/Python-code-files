import pandas as pd 
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

data = pd.read_csv("conv.csv")
print(data)

cv = CountVectorizer()
vector = cv.fit_transform(data['qts'])

print("welcome to kc --> chityy, enter your question and press q for quit")
while True:
    qts = input("qts --> " )
    if qts == "q":
        print("chitty --> bye ")
        break
    else:
        vqts = cv.transform([qts])
        cs = cosine_similarity(vqts, vector)
        fcs = cs.flatten()
        indices = np.argpartition(fcs, -1)[-1:]
        res = data.iloc[indices]
        print(" ".join(res["ans"]))

