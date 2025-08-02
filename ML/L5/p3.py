# data ppoint and predict

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("pos_salary.csv")
print(data)

feature = data[["Level"]]
target = data[["Salary"]]

model = LinearRegression()
model.fit(feature,target)

plt.scatter(data[["Level"]], data[["Salary"]], color = "red")
plt.plot(data[["Level"]], model.predict(feature), color = "blue")
plt.show()


print(model.predict([[3]]))
print(model.predict([[9]]))
print(model.predict([[10]]))

