
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("pos_salary.csv")
print(data)

feature = data[["Level"]]
target = data[["Salary"]]

pf = PolynomialFeatures(degree = 5)
new_feature = pf.fit_transform(feature)
print(new_feature)

model = LinearRegression()
model.fit(new_feature,target)

plt.scatter(data[["Level"]],data[["Salary"]], color = "red")
plt.plot(data[["Level"]], model.predict(new_feature), color = "blue")
plt.show()

level = [[3]]
new_level = pf.fit_transform(level)
print(model.predict(new_level))

level = [[9]]
new_level = pf.fit_transform(level)
print(model.predict(new_level))


