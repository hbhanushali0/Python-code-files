
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


data = pd.read_csv("result_data.csv")

feature = data[["hr"]]
target = data["result"]

model = LogisticRegression()
model.fit(feature,target)

y_pred = model.predict(feature)

plt.scatter(data["hr"], data["result"])
plt.plot(data["hr"], y_pred)
plt.xlabel("Hours")
plt.ylabel("Result")
plt.title("Hours vs Result")
plt.show()


