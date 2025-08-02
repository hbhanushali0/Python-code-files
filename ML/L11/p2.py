
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


data = pd.read_csv(("loan_default_data.csv"))
print(data)
print(data.isnull().sum())

features = data[["GENDER", "OCCUPATION"]]
target = data["DEFAULT"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

print(target)

x_train,x_test, y_train, y_test = train_test_split(new_features,target)


model = DecisionTreeClassifier()
abc = model.fit(x_train,y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)


gen = int(input("0 female , 1 male "))
occ = int(input("0 business , 1 salary "))
d = model.predict([[gen,occ]])
print(d)




