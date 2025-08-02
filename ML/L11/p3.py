
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv(("loan_default_data.csv"))
print(data)
print(data.isnull().sum())

features = data[["GENDER", "OCCUPATION"]]
target = data["DEFAULT"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

print(target)

model = RandomForestClassifier(n_estimators = 100)
abc = model.fit(new_features,target)

gen = int(input("0 female , 1 male "))
occ = int(input("0 business , 1 salary "))
d = model.predict([[gen,occ]])
print(d)
