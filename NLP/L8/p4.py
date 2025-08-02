#import lib
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np 

#load the data
data = pd.read_csv('movies.csv')
print(data)

#check null data
print(data.isnull().sum())

#clean the data
def clean_data(txt):
    txt = txt.lower()
    txt = re.sub("[^A-z ]", " ", txt)
    return txt

data['clean_title'] = data['title'].apply(clean_data)
print(data)

#text vectorization
tv = TfidfVectorizer()
vector = tv.fit_transform(data['clean_title'])
print(vector)

#ask for movie name
mn = input(" enter movie name ")
cmn = clean_data(mn)
vmn = tv.transform([cmn])
print(vmn)

#suggest the movie
if vmn.nnz == 0:
    print(" movie does not exist")
else:
    cs = cosine_similarity(vmn, vector)
    print(cs)

    fcs = cs.flatten()
    print(fcs)

    indices = np.argpartition(fcs, -5)[-5:]
    print(indices)

    movies = data.iloc[indices][::-1]
    print(movies)

