
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, classification_report

data = pd.read_csv("vehicle_data.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["Age"]]
target = data["Vehicle"]

x_train, x_test, y_train, y_test = train_test_split(feature,target,random_state = 123)

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


