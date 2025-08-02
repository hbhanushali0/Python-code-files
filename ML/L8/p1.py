
import pandas as pd
from sklearn.naive_bayes import BernoulliNB


data = pd.read_csv("play_data.csv")
print(data)

feature = data[["Weather"]]
target = data["Play"]

new_feature = pd.get_dummies(feature, drop_first = True)
print(new_feature)

model = BernoulliNB()
model.fit(new_feature,target)

we = int(input("1 overcast 2 rainy 3 sunny  "))
if we == 1:
    d = [[0,0]]
elif we == 2:
    d = [[1,0]]
else:
    d = [[0,1]]
    
print(d)

ans = model.predict(d)
print(ans)
print(model.predict_proba(d))


