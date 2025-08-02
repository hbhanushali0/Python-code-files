
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


data = pd.read_csv("shareprice1.csv")
print(data)


feature = data[["year"]]
target = data["adani"]

'''
plt.scatter(feature, target)
plt.show()

'''


x_train, x_test, y_train, y_test = train_test_split(feature,target)

model = DecisionTreeRegressor()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cr = classification_report(y_test,y_pred)
print(cr)




d = int(input("enter year "))

res = model.predict([[d]])

print("price = ", res)


