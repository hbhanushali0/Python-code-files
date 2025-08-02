
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("result_data.csv")
print(data)
print(data.isnull().sum())

feature = data[["hr"]]
target = data["result"]

x_train, x_test, y_train, y_test = train_test_split(feature,target)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test,y_pred)
print(cr)







