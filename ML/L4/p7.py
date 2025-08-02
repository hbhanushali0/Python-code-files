


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

data = pd.read_csv("fruit_qty_prices.csv")
print(data)

imp1 = SimpleImputer(missing_values = np.nan, strategy = "most_frequent")
data[["name"]] = imp1.fit_transform(data[["name"]])
print(data)

imp2 = SimpleImputer(missing_values = np.nan, strategy = "median")
data[["price"]] = imp2.fit_transform(data[["price"]])
print(data)

features = data[["name", "quantity"]]
print(features)

ct = ColumnTransformer([("name", OneHotEncoder(),[0])], remainder = "passthrough")

new_features = ct.fit_transform(features)
print(features)

new_features = pd.DataFrame(new_features[:,1:], columns = ["Mango", "quantity"])
print(new_features)

target = data[["price"]]

x_train, x_test, y_train, y_test = train_test_split(new_features,target,random_state = 120)

model = LinearRegression()
model.fit(x_train,y_train)


train_score = model.score(x_train,y_train)
print("train_score = ", train_score)

test_score = model.score(x_test, y_test)
print("test_score = ", test_score)

qty = float(input("enter qty "))
fruit = input("1 Apple and 2 Mango  ")
if fruit == 1:
    d = [0,qty]
else:
    d = [1,qty]

price = model.predict([d])
print("price = ", price)


