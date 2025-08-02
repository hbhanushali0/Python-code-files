
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("cricketers_data.csv")
print(data)

print(data.isnull().sum())

plt.scatter(data["RUNS"], data["WICKETS"])
plt.show()

features = data[["RUNS", "WICKETS"]]

scaler = MinMaxScaler()
new_features = scaler.fit_transform(features)

print(features)

print(new_features)

model = KMeans(n_clusters = 2)
result = model.fit_predict(new_features)


data["cluster"] = result
print(data)

plt.scatter(data["RUNS"], data["WICKETS"], c = data["cluster"])
plt.xlabel("runs")
plt.ylabel("wickets")
plt.title("final scatter")
plt.show()

r = int(input("enter runs  "))
w = int(input("enter wickets "))
d = [[r,w]]
new_d = scaler.transform(d)
print(model.predict(new_d))











