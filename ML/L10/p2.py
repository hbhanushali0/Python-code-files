
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


data = pd.read_csv("health_data.csv")
print(data.head())

print(data.isnull().sum())

features = data[["Weight", "Height"]]
target = data["Class"]

scaler = MinMaxScaler()
new_features = scaler.fit_transform(features)
print(new_features)

x_train, x_test, y_train, y_test = train_test_split(new_features,target)

# find the value of k

num, tr_score, te_score = [], [] ,[]
for i in range(1, len(x_train)):
    model = KNeighborsClassifier(n_neighbors = i, metric = "euclidean")
    model.fit(x_train, y_train)
    trs = model.score(x_train, y_train)
    tes = model.score(x_test, y_test)
    num.append(i)
    tr_score.append(trs)
    te_score.append(tes)
    

print(num)
print(tr_score)
print(te_score)

import matplotlib.pyplot as plt

plt.plot(num, tr_score, label = "training score", color = "red")
plt.plot(num, te_score, label = "testing score", color = "blue")
plt.legend()
plt.show()


