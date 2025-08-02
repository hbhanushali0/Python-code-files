#import lilb
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
pd.set_option('max_colwidth',1000)
from sklearn.metrics import classification_report

#load the data
data = pd.read_csv('hr2_ap24.csv')
print(data)

#check null data
print(data.isnull().sum())


#gps

sia = SentimentIntensityAnalyzer()
def gps(txt):
    ps = sia.polarity_scores(txt)
    return ps


data['polarity_scores'] = data['review'].apply(gps)
print(data)


#gs
def gs(txt):
    ps = sia.polarity_scores(txt)
    if ps['compound'] >= 0.05:
        return "pos"
    elif ps['compound'] <= -0.05:
        return "neg"
    else:
        return "neu"

data['sia_label'] = data['review'].apply(gs)
print(data)

data.to_csv("hr2.csv", index=False)

# compare label vs sia_label
cr = classification_report(data['label'], data['sia_label'])
print(cr)

cr = classification_report(data['sia_label'], data['label'])
print(cr)

