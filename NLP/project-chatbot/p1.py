import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

data = pd.read_csv("project_dataset.csv")


cv = CountVectorizer()
vector = cv.fit_transform(data['Question'])

print("Welcome to Py-bot --> 'A chat bot for python language -> ask right away or press 'q' to exit'")
while True:
    q = input("please ask your question ")
    if q == "q":
        print("Pybot --> bye")
        break
    else:
        vq = cv.transform([q])
        cs = cosine_similarity(vector, vq)
        fcs = cs.flatten()
        indices = np.argpartition(fcs, -1)[-1:]
        res = data.iloc[indices]
        print(" ".join(res["Answer"]))
