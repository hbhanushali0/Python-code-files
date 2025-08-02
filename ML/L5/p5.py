
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

data = pd.read_csv("pos_salary.csv")
print(data)

feature = data[["Level"]]
target = data[["Salary"]]

pf = PolynomialFeatures(degree = 5)

new_feature = pf.fit_transform(feature)
print(new_feature)

x_train, x_test, y_train, y_test = train_test_split(new_feature,target,random_state = 29)

model = LinearRegression()
model.fit(x_train, y_train)


train_score = model.score(x_train,y_train)
print("train_score = ", train_score)

test_score = model.score(x_test,y_test)
print("test_score = ", test_score)


level = float(input("enter level  "))

new_level = pf.fit_transform([[level]])


salary = model.predict(new_level)
print("salary =  ", salary)





