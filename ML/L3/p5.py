
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("apple_prices.csv")
print(data)


data.dropna(how = "any", axis = 0, inplace = True)
print(data)



feature = data[["quantity"]]
target = data[["price"]]

x_train, x_test, y_train, y_test = train_test_split(feature,target)

model = LinearRegression()
model.fit(x_train, y_train)

qty = int(input("please enter quantity  "))
p = model.predict([[qty]])
print(p)



