#import lib
import pandas as pd 
import re
from sklearn.feature_extraction.txt import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

#load the data
data = pd.read_csv("movies.csv")
print(data)

#check for null
print(data.isnull().sum())

#clean the title
def clean_title(txt):
    txt = txt.lower()
    txt = re.sub("[^A-Za-z ]", "", txt)
    return txt


data['clean_title'] = data['title'].apply(clean_title)
print(data['clean_title'])

#clean the genre
def clean_genres(txt):
    txt = txt.lower()
    txt = re.sub("[ | ]", "", txt)
    return txt

data['clean_genres'] = data['genres'].apply(clean_genres)
print(data['clean_genres'])

#vectorize the genre
tv = TfidfVectorizer()
vector = tv.fit_transform(data['clean_genres'])
print(vector)

#ask for movie title
title = input(" enter movie title ")
ctitle = clean_title(title)

#search for genre
genres = data[data.clean_title.str.contains(ctitle)]
print(genres)
print(genres.shape)

#recommend the movies
if(genres.shape[0] == 0):
    print("movie does not exists")
else:
    ag = " ".join(genres['clean_genres'])
    print(ag)

    vag = tv.transform([ag])
    print(vag)

    cs = cosine_similarity(vag, vector)
    print(cs)

    fcs = cs.flatten()
    print(fcs)

    indices = np.argpartition(fcs, -20)[-20:]
    print(indices)

    result = data.iloc[indices][::-1]
    print(result['title'])


    