# missing data and categorical data using pandas


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("fruit_qty_prices.csv")
print(data)

data .fillna({"name": "Mango","price": data["price"].mean()}, inplace = True)
print(data)

dummies = pd.get_dummies(data.name, drop_first = True)
print(dummies)

new_data = pd.concat([data , dummies], axis = "columns")
print(new_data)
new_data = new_data.drop(["name"], axis = "columns")
print(new_data)

features = new_data[["quantity", "Mango"]]
target = new_data[["price"]]

print(features)
print(target)

x_train, x_test, y_train, y_test = train_test_split(features,target,random_state = 12)

model = LinearRegression()
model.fit(features,target)

train_score = model.score(x_train,y_train)
print("train_score = ", train_score)

test_score = model.score(x_test,y_test)
print("test_score = ", test_score)


qty = float(input("enter qty  "))
fruit = input("1 Apple and 2 Mango  ")

if fruit == 1:
    d = [qty,0]
    
else:
    d = [qty,1]
    
price = model.predict([d])

print("price = ", round(price.item(),2))



    


