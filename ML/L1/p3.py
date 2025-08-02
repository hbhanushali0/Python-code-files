
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("home_prices_1.csv")

feature = data[["area"]]
target = data[["price"]]

x_train, x_test, y_train, y_test = train_test_split(feature,target,random_state = 120)
print(x_train)
print(y_train)

print(x_test)
print(y_test)

model = LinearRegression()
model.fit(x_train, y_train)

score = model.score(x_test, y_test)
print("score = ", score)
print("score = ", score * 100)

area = float(input("please enter area  "))
price = model.predict([[area]])
print("price = ", price)


