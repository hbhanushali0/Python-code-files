#tv

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('kcfb_ap24.csv')
print(data)

print()

tv = TfidfVectorizer()
tvector = tv.fit_transform(data['text'])

features = pd.DataFrame(tvector.toarray(), columns = tv.get_feature_names())
print(features)

