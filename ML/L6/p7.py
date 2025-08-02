
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("insurance_data.csv")

feature = data[["age"]]
target = data["have_insurance"]

model = LogisticRegression()
model.fit(feature,target)

age = float(input("enter age "))
res = model.predict([[age]])
print(res)


