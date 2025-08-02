
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv("apple_prices.csv")
print(data)

imp1 = SimpleImputer(missing_values = np.nan, strategy = "mean")
data[["price"]] = imp1.fit_transform(data[["price"]])
print(data)

feature = data[["quantity"]]
target = data[["price"]]

x_train, x_test, y_train, y_test = train_test_split(feature,target)

model = LinearRegression()
model.fit(x_train,y_train)


qty = int(input("please enter quantity  "))
p = model.predict([[qty]])
print(p)


