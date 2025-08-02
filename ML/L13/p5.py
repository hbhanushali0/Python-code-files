
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("xy_data.csv")
print(data)

print(data.isnull().sum())

features = data[["X", "Y"]]

num, val = [], []
for i in range(1,8):
    model = KMeans(n_clusters = i)
    model.fit(features)
    print(model.inertia_)
    num.append(i)
    val.append(model.inertia_)
    
plt.plot(num, val)
plt.xlabel("no of clusters")
plt.ylabel("inertia")
plt.show()



