
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


x_train, x_test, y_train, y_test = train_test_split(new_features, target, random_state = 123)

model = KNeighborsClassifier(n_neighbors = 17, metric = "euclidean")
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)

p = int(input("enter pregnancies  "))
g = float(input("enter glucose  "))
b = float(input("enter bloodpressure "))
s = float(input("enter skin thickness  "))
i = float(input("enter insulin  "))
bmi = float(input("enter bmi  "))
d = float(input("enter diabetes p function "))
a = int(input("enter age  "))

d = [[p,g,b,s,i,bmi,d,a]]

t_d = scaler.transform(d)

print(model.predict(t_d))


