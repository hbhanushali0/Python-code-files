
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("salary_1.csv")
print(data)

feature = data[["exp"]]
target = data[["salary"]]

print(feature)
print(target)

model = LinearRegression()
model.fit(feature,target)

b0 = model.intercept_
b1 = model.coef_

print("bo = ", b0)
print("b1 = ", b1)

e = float(input("please enter experience  "))
s = model.predict([[e]])
print("salary =  ", s)


