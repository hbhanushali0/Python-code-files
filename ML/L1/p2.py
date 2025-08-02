
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("home_prices_1.csv")

feature = data[["area"]]
target = data[["price"]]

model = LinearRegression()
model.fit(feature,target)

b0 = model.intercept_
b1 = model.coef_

print("b0 = ", b0)
print("b1 = ", b1)

area = float(input("please enter area "))
price1 = model.predict([[area]])
print("price1 = ", price1)

price2 = b0 + b1 * area
print("price2 = ", price2)


