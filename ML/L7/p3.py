

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, classification_report


data = pd.read_csv("age_movie.csv")
print(data)

imp1 = SimpleImputer(missing_values = np.nan, strategy = "mean")
data[["age"]] = imp1.fit_transform(data[["age"]])
print(data)

imp2 = SimpleImputer(missing_values = np.nan, strategy = "constant", fill_value = "moneyheist")
data[["movie"]] = imp2.fit_transform(data[["movie"]])
print(data)

feature = data[["age"]]
target = data["movie"]

x_train, x_test, y_train, y_test = train_test_split(feature,target,random_state = 23)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(x_test)
print(y_test)
print(y_pred)

cm = confusion_matrix(y_test, y_pred)
print(cm)

plot_confusion_matrix(model, x_test, y_test)
plt.show()

cr = classification_report(y_test, y_pred)
print(cr)

age = float(input("enter age "))
print(model.predict([[age]]))

res = model.predict_proba([[age]]).ravel().tolist()
for r  in res:
    print(round(r,4))




