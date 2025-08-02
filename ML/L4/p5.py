
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

data = pd.read_csv("place_area_price.csv")
print(data)

features = data[["place","area"]]
ct = ColumnTransformer([("place", OneHotEncoder(),[0])], remainder = "passthrough")
new_features = ct.fit_transform(features)

new_features = pd.DataFrame(new_features[:, 1:], columns = ["khandala","lonavala", "area"])
print(new_features)

target = data[["price"]]
print(target)

model = LinearRegression()
model.fit(new_features,target)


area = float(input("please enter area  "))
place = input("1 lonavala, 2 karjat, 3 khandala  ")
if place == 1:
    d = [0,1,area]
elif place == 2:
    d = [0,0,area]
else:
    d = [1,0,area]
    
price = model.predict([d])
print("price =  ", price)


