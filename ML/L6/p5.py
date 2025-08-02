
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, classification_report, accuracy_score, precision_score, recall_score

data = pd.read_csv("result_data.csv")

feature = data[["hr"]]
target = data["result"]

x_train, x_test, y_train, y_test = train_test_split(feature, target)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

plot_confusion_matrix(model, x_test, y_test)
plt.show()

cr = classification_report(y_test, y_pred)
print(cr)

asc = accuracy_score(y_test, y_pred)
print(asc)

pcf = precision_score(y_test, y_pred, pos_label = "fail")
print(pcf)

pcp = precision_score(y_test, y_pred, pos_label = "pass")
print(pcp)


