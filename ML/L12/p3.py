

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv("result_data.csv")
print(data)
print(data.isnull().sum())

feature = data[["hr"]]
target = data["result"]

model = RandomForestClassifier()
abc = model.fit(feature,target)

hr = float(input("enter hours "))
d = [[hr]]
print(model.predict(d))





