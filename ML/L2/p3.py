
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("salary_1.csv")
print(data)

feature = data[["exp"]]
target = data[["salary"]]

x_train, x_test, y_train, y_test = train_test_split(feature, target, random_state = 101)
print(x_train)
print(y_train)

print(x_test)
print(y_test)

model = LinearRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print("train score = ", train_score)

test_score = model.score(x_test, y_test)
print("test score = ", test_score)


e = float(input("please enter experience  "))
s = model.predict([[e]])
print("salary = ", s)
print("salary = ", s.item())
print("salary = ", round(s.item(),2))



