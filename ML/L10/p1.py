

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("health_data.csv")
print(data.head())

print(data.info())
print(data.isnull().sum())

features = data[["Weight", "Height"]]
target = data["Class"]

print(features)
print(target)

scaler = MinMaxScaler()
new_features = scaler.fit_transform(features)

print(new_features)

model = KNeighborsClassifier(n_neighbors = 3, metric = "euclidean")
model.fit(new_features,target)
we = float(input("enter weight  "))
he  = float(input("enter height  "))
d = [[we,he]]
t_d = scaler.transform(d)

print(model.predict(t_d))
print(model.kneighbors(t_d, n_neighbors = 3))

