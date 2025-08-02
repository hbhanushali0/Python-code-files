

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("xy_data.csv")
print(data)

print(data.isnull().sum())

plt.scatter(data["X"], data["Y"])
plt.show()

features = data[["X", "Y"]]

model = KMeans(n_clusters = 2)
result = model.fit_predict(features)
print(result)

data["cluster"] = result
print(data)

plt.scatter(data["X"], data["Y"], c = data["cluster"])
plt.show()

centroids = model.cluster_centers_
print(centroids)
