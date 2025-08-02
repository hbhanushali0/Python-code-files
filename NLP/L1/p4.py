import pandas as pd
from nltk import word_tokenize

data = pd.read_csv('abp3.csv')
print(data)



def clean_data(txt):
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in ['area','bedrooms']]
    txt = ','.join(txt)
    return txt





data['clean_info'] = data['info'].apply(clean_data)
print(data)

data[['area','bedrooms']] = data['clean_info'].str.split(',',expand=True)
print(data)
