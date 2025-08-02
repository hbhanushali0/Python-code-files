import pandas as pd
from sklearn.linear_model import LinearRegression
from nltk import word_tokenize
from string import punctuation

data = pd.read_csv('abp2.csv')
print(data)

def clean_data(txt):
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = ','.join(txt)
    return txt





data['clean_info'] = data['info'].apply(clean_data)
print(data)

data[['area','bedrooms']] = data['clean_info'].str.split(',',expand=True)
print(data)

