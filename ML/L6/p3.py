

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("result_data.csv")
print(data)

feature = data[["hr"]]
target = data["result"]

model = LogisticRegression()
model.fit(feature,target)

hours = float(input("enter hours "))
result = model.predict([[hours]])
print(result)

#  1 / 1 + e ^ -(b0 + b1 * x)

b0 = model.intercept_
b1 = model.coef_

lf = 1 / (1 +(2.71 ** (-1 * (b0 + b1 * hours))))
print(lf)

if lf > 0.5:
    print("pass")
    
else:
    print("fail")
    

