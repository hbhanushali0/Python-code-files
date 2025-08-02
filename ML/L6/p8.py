

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

b0 = model.intercept_
b1 = model.coef_

lf = 1 / (1 + (2.71 ** (-1 * (b0 + b1 * age))))
print(lf)

if lf > 0.5:
    print("yes")
    
else:
    print("no")
    

