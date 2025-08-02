#import lilb
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
pd.set_option('max_colwidth',1000)

#load the data
data = pd.read_csv('hr1_ap24.csv')
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

data['Sentiments'] = data['review'].apply(gs)
print(data)

data.to_csv("hr1.csv", index=False)

