
import pandas as pd
from sklearn.linear_model import LinearRegression

data= pd.read_csv("place_area_price.csv")

new_dummies = pd.get_dummies(data.place, drop_first = True)
new_data = pd.concat([data, new_dummies], axis = "columns")
new_data = new_data.drop(["place"], axis = "columns")

print(data)
print(new_data)

features = new_data[["area", "Khandala", "Lonavala"]]
target = new_data[["price"]]

model = LinearRegression()
model.fit(features,target)

area = float(input("please enter area  "))
location = input("1 karjat, 2 khandala, 3 lonavala")
if location == 1:
    d = [area,0,0]
elif location == 2:
    d = [area,1,0]
else:
    d = [area,0,1]
    
price = model.predict([d])
print("price =  ", price)


