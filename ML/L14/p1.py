
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

plt.scatter(data["A"], data["B"], color = "red")
plt.xlabel("A")
plt.ylabel("B")
plt.show()

cr = model.cluster_centers_
print(cr)



