#import lib
import pandas as pd 
from wordcloud import *
import matplotlib.pyplot as plt

#load the data
data = pd.read_csv("hr1.csv")
print(data)

#get positive data
pos_data = data[data.Sentiments == "pos"]
print(pos_data)
pos_reviews = " ".join(pos_data['review'])
print(pos_reviews)

#generate wc
wc1 = WordCloud(max_words=7, width=800, height=400, background_color = "white", colormap="Set2").generate(pos_reviews)
plt.figure(figsize=(10,5))
plt.axis("off")
plt.imshow(wc1)
plt.savefig("wpos.png")

#get negative data
pos_data = data[data.Sentiments == "neg"]
print(pos_data)
pos_reviews = " ".join(pos_data['review'])
print(pos_reviews)

#generate wc
wc2 = WordCloud(max_words=7, width=800, height=400, background_color = "white", colormap="Set2").generate(pos_reviews)
plt.figure(figsize=(10,5))
plt.axis("off")
plt.imshow(wc2)
plt.savefig("wneg.png")
