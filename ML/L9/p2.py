

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report

data = pd.read_csv("email_data.csv")
print(data.head())

data.drop("Mn",axis = "columns",  inplace = True)

print(data.isnull().sum())

features = data.drop("Result", axis = "columns")
target = data["Result"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

x_train, x_test, y_train, y_test = train_test_split(new_features, target, random_state = 123)

model = BernoulliNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)



d = int(input("1 dear = yes 0 no  "))
f = int(input("1 friend = yes 0 no "))
l = int(input("1 lunch = yes  0 no  "))
m = int(input("1 money = yes  0 no  "))

res = [[d,f,l,m]]
print(model.predict(res))
print(model.predict_proba(res))

'''
d = [[1,1,1,1]]
print(model.predict(d))
print(model.predict_proba(d))
'''
