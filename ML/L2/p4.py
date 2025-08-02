
import pandas as pd
from sklearn.linear_model import LinearRegression


data = pd.read_csv("home_prices_1.csv")
print(data)

features = data[["area","bedrooms"]]
target = data[["price"]]

print(features)
print(target)

model = LinearRegression()
model.fit(features,target)

b0 = model.intercept_
b1 = model.coef_

print("b0 = ", b0)
print("b1 = ", b1)

a = float(input("please enter area   "))
b = float(input("please enter bedroom  "))
p = model.predict([[a,b]])
print("price = ",p)

