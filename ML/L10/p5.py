
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("weight_data.csv")
print(data.head())
print(data.isnull().sum())

features = data[["HEIGHT", "AGE"]]
target = data["WEIGHT"]

scaler = MinMaxScaler()
new_features = scaler.fit_transform(features)
print(new_features)

x_train, x_test, y_train, y_test = train_test_split(new_features, target, random_state = 99)

model = KNeighborsRegressor(n_neighbors = 3, metric = "euclidean")
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("training score = ", model.score(x_train, y_train))
print("testing score = ", model.score(x_test, y_test))


he = float(input("enter height  "))
we = float(input("enter age  "))
d = [[he, we]]
t_d = scaler.transform(d)

print(model.predict(t_d))
print(model.kneighbors(t_d, n_neighbors = 3))



