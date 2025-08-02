
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("result_data.csv")
print(data)

feature = data[["hr"]]
target = data["result"]

print(feature)
print(target)

model = LogisticRegression()
model.fit(feature,target)

hours = float(input("enter hours "))
result = model.predict([[hours]])
print(result)

