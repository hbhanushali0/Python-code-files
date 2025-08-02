
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv("run_data.csv")
print(data)
print(data.isnull().sum())

features = data[["Weather","Just Ate"]]
target = data["Will I Go Running?"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

model = RandomForestClassifier()
abc = model.fit(new_features,target)


we = int(input("0 rainy 1 sunny "))
ja = int(input("0 no  1 yes "))
d = [[we,ja]]
print(model.predict(d))



