
import pandas as pd
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("go_sh_data.csv")
print(data)

features = data[["Weather", "Car"]]
target = data["Result"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

model = BernoulliNB()
model.fit(new_features,target)

w = int(input("1 sunny 2 rainy "))
c = int(input("1 working 2 broken "))

if w == 1 & c == 1:
    d = [[1,1]]
elif w == 1 & c == 2:
    d = [[1,0]]
elif w == 2 & c == 1:
    d = [[0,1]]
else:
    d = [[0,0]]
    
ans = model.predict(d)
print(ans)



