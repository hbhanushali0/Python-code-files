

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("tshirt_data.csv")
print(data)

data.drop("Person",axis = "columns", inplace = True)
print(data)

features = data.drop("T-Shirt Size", axis = "columns")
target = data["T-Shirt Size"]

# feature scaling

scaler = MinMaxScaler()
s_features = scaler.fit_transform(features)
print(s_features)

new_features = pd.DataFrame(s_features, columns= ["Height(cm)", "Weight(kg)"])
print(new_features, type(new_features))

model = KNeighborsClassifier(n_neighbors = 3, metric = "euclidean")
model.fit(new_features,target)

ht = float(input("enter height in cms  "))
wt = float((input("enter weight in kgs  ")))

d = [[ht, wt]]
new_d = scaler.transform(d)
print(d, new_d)

print(model.predict(new_d))

# shows which nearest data points are used

print(model.kneighbors(new_d, n_neighbors= 3))

