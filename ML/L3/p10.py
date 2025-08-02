

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("exp_test_sal.csv")
print(data)

imp1 = SimpleImputer(missing_values = np.nan, strategy = "mean")
data[["test"]] = imp1.fit_transform(data[["test"]])
data[["salary"]] = imp1.fit_transform(data[["salary"]])
print(data)


features = data[["exp", "test"]]
target = data[["salary"]]

x_train, x_test, y_train, y_test = train_test_split(features, target)

model = LinearRegression()
model.fit(x_train,y_train)

e = float(input("please enter experience  "))
t = float(input("please enter test score  "))
s = model.predict([[e,t]])

print("Salary = ", s)


