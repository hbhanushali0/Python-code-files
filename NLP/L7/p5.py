#import lib
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import * 
import matplotlib.pyplot as plt 

#load the data
data = pd.read_csv("tar_ap24.csv")
print(data)

#check null data
print(data.isnull().sum())

#gs
sia = SentimentIntensityAnalyzer()
def gs(txt):
    ps = sia.polarity_scores(txt)
    if ps['compound'] >= 0.05:
        return 'pos'
    elif ps['compound'] <= -0.05:
        return 'neg'
    else:
        return "neu"
    
data['sentiments'] = data['Review'].apply(gs)
print(data)

#get positive data
pos_data = data[data.sentiments == 'pos']
print(pos_data)
pos_reviews = " ".join(pos_data['Review'])
print(pos_reviews)

#generate wc
wc1 = WordCloud(max_words=20, width=800, height=400, background_color= "white", ).generate(pos_reviews)
plt.figure(figsize=(10,5))
plt.axis("off")
plt.imshow(wc1)
plt.savefig("tr_wcpos.png")

