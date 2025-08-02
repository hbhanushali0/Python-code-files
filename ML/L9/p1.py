
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

data = pd.read_csv("Social_Network_Ads.csv")
print(data.head())  # first five values
print(data.shape)  # (no rows, no columns)

data.drop("User ID", axis = "columns", inplace = True)

print(data.info())
print(data.isnull().sum())


features = data.drop("Purchased", axis = "columns")
target = data["Purchased"]

new_features = pd.get_dummies(features , drop_first = True)
print(new_features.head())

x_train, x_test, y_train, y_test = train_test_split(new_features, target)

model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)

age = float(input("enter age  "))
est_sal = float(input("enter estimated salary  "))
gender = int(input("0 female 1 male  "))

if gender == 0:
    d = [[age, est_sal, 0]]
else:
    d = [[age, est_sal, 1]]
    
print(model.predict(d))
print(model.predict_proba(d))




