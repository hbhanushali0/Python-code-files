
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("diabetes.csv")
print(data.head())

print(data.info())
print(data.isnull().sum())



data[["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]] = data[["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]].replace(0, np.NAN)
print(data.isnull().sum())

data["Glucose"].fillna(data["Glucose"].mean(),inplace = True)
data["BloodPressure"].fillna(data["BloodPressure"].mean(), inplace = True)
data["SkinThickness"].fillna(data["SkinThickness"].mean(), inplace = True)
data["Insulin"].fillna(data["Insulin"].mean(), inplace = True)
data["BMI"].fillna(data["BMI"].mean(), inplace = True)

print(data.isnull().sum())




features = data.drop("Outcome", axis = "columns")
target = data["Outcome"]
print(features.head())
print(target.head())

scaler = MinMaxScaler()
new_features = scaler.fit_transform(features)
print(new_features)


# find the value of k

x_train, x_test, y_train, y_test = train_test_split(new_features, target)

num, tr_score, te_score = [], [], []
for i in range(1,30):
    model = KNeighborsClassifier(n_neighbors = i)
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

