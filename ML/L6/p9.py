

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("insurance_data.csv")

feature = data[["age"]]
target = data["have_insurance"]

x_train, x_test, y_train, y_test = train_test_split(feature,target)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(x_test)
print(y_test)
print(y_pred)



cr = classification_report(y_test,y_pred)
print(cr)

