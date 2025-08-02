

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("ab_data.csv")
print(data)

print(data.isnull().sum())

plt.scatter(data["A"], data["B"], color = "red")
plt.xlabel("A")
plt.ylabel("B")
features = data[["A","B"]]

model = KMeans(n_clusters = 3)
result = model.fit_predict(features)
print(result)

data["cluster"] = result
print(result)

a1 = float(input("enter value of a "))
b1 = float(input("enter value of b  "))
d = [[a1,b1]]
print(model.predict(d))

