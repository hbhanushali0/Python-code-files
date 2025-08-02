
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("car_data.csv")
print(data.head())

data.columns = ["buying","maintenance","doors","persons","lug_boot","safety","class"]

print(data.isnull().sum())

features = data.drop("class", axis = "columns")
target = data["class"]

print(features.head())
print(target.head())

new_features = pd.get_dummies(features, drop_first = True)
print(new_features.head())

x_train, x_test, y_train, y_test = train_test_split(new_features, target)

model = RandomForestClassifier()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)

fi = model.feature_importances_
x = new_features.columns
y = fi
plt.barh(x,y)
plt.show()

sel_features = new_features[["safety_low", "persons_4"]]

x_train, x_test, y_train, y_test = train_test_split(sel_features, target)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)

