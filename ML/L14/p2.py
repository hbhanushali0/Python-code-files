
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv("ab_data.csv")
print(data)

print(data.isnull().sum())

plt.scatter(data["A"], data["B"], color = "red")
plt.xlabel("A")
plt.ylabel("B")
plt.show()

features = data[["A", "B"]]

model = KMeans(n_clusters = 3)
result = model.fit_predict(features)
print(result)

data["cluster"] = result
print(result)

data0 = data[data.cluster==0]
data1 = data[data.cluster==1]
data2 = data[data.cluster==3]

print(data0)
print(data1)
print(data2)

plt.scatter(data0["A"], data0["B"], color = "red")
plt.scatter(data1["A"], data1["B"], color = "green")
plt.scatter(data2["A"], data2["B"], color = "blue")
plt.xlabel("A")
plt.ylabel("B")
plt.title("final cluster")
plt.show()

cr = model.cluster_centers_
print(cr)



