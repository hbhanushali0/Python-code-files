
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("go_sh_wm.csv")
print(data)

features = data[["Weather", "Car"]]
target = data["Result"]

new_features = pd.get_dummies(features, drop_first = True)

model = BernoulliNB()

x_train, x_test, y_train, y_test = train_test_split(new_features,target, random_state = 101)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)


cr = classification_report(y_test, y_pred)
print(cr)


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
