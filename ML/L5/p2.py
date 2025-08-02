# linear regression fails

import pandas as pd
from sklearn.linear_model import LinearRegression


data = pd.read_csv("pos_salary.csv")
print(data)

feature = data[["Level"]]
target = data[["Salary"]]

print(feature)
print(target)


model = LinearRegression()
model.fit(feature,target)

l = float(input("enter level  "))
s = model.predict([[l]])
print("Salary =  ", s)

