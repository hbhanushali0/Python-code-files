

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

features = data[["A","B"]]

num, val = [], []
for i in range(1,9):
    model = KMeans(n_clusters = i)
    model.fit(features)
    num.append(i)
    val.append(model.inertia_)
    
plt.plot(num,val)
plt.xlabel("no of clusters ")
plt.ylabel("inertia ")
plt.show()

