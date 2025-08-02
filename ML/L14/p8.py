
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("dosage_eff_data.csv")
print(data)

print(data.isnull().sum())

plt.scatter(data["dos"], data["eff"])
plt.show()

feature = data[["dos"]]
target = data["eff"]

m1 = LinearRegression()
m1.fit(feature,target)
print(m1.predict([[6]]))

m2 = DecisionTreeRegressor()
m2.fit(feature,target)
print(m2.predict([[6]]))

m3 = RandomForestRegressor()
m3.fit(feature,target)
print(m3.predict([[6]]))








