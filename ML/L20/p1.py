
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

data = pd.read_csv("diabetes.csv")
print(data.head())

print(data.isnull().sum())

features = data[["FS","FU"]]
target = data["Diabetes"]

print(features.head())
print(target.head())

new_features = pd.get_dummies(features, drop_first = True)

print(new_features.head())

x_train,x_test, y_train,y_test = train_test_split(new_features, target, random_state = 123)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test, y_pred)
print(cr)

with open("db.model", "wb") as f:
    pickle.dump(model,f)
    
    
