
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("exp_test_sal.csv")
print(data)

data.dropna(how = "any", inplace = True)
print(data)

features = data[["exp","test"]]
target = data[["salary"]]

x_train, x_test, y_train, y_test = train_test_split(features,target)

model = LinearRegression()
model.fit(x_train, y_train)

e = float(input("please enter experience  "))
t = float(input("please enter your test  "))
s = model.predict([[e,t]])

print("salary =  ", s)


