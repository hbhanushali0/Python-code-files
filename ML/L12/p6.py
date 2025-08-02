


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

data = pd.read_csv("titanic_data.csv")
print(data.head())
print(data.shape)

data.drop(["PassengerId", "Name", "Ticket", "Cabin", "Pclass", "SibSp", "Parch", "Embarked"], axis = "columns", inplace = True)

print(data.isnull().sum())
print(data.head())

data.fillna({"Embarked": "S"}, inplace = True)
data.fillna({"Age": data["Age"].mean()}, inplace = True)

print(data.isnull().sum())

features = data[["Age", "Sex", "Fare"]]
target = data["Survived"]

print(features.head())
print(target.head())


new_features = pd.get_dummies(features, drop_first = True)
print(new_features.head())

x_train, x_test, y_train, y_test = train_test_split(new_features, target, random_state = 33)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)


