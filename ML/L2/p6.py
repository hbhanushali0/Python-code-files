
import pandas as pd
from sklearn.linear_model import LinearRegression


data = pd.read_csv("new_exp_test_sal.csv")
print(data)

features = data[["exp","test"]]
target = data[["salary"]]

print(features)
print(target)

model = LinearRegression()
model.fit(features,target)

b0 = model.intercept_
b1 = model.coef_

print("bo = ", b0)
print("b1 = ", b1)

e = float(input("please enter experience "))
t = float(input("please enter test result "))
s = model.predict([[e,t]])
print("salary = ",s)

