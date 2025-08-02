import pandas as pd 
from nltk import word_tokenize
from string import punctuation
from nltk.corpus import stopwords



data = pd.read_csv('abp5.csv')
print(data)


def clean_data(txt):
    txt = txt.lower()
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = [t for t in txt if t not in stopwords.words('english')]
    txt = [t for t in txt if t not in ['area', 'bedrooms']]
    txt = ','.join(txt)
    return txt


data['clean_info'] = data['info'].apply(clean_data)
print(data)

data[['area','bedrooms']] = data['clean_info'].str.split(',',expand=True)
print(data)