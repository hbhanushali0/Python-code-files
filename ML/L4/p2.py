
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("place_area_price.csv")
print(data)

dummies = pd.get_dummies(data.place)
print(dummies)

new_dummies = pd.get_dummies(data.place, drop_first = True)
print(new_dummies)

new_data = pd.concat([data,new_dummies], axis = "columns")
print(new_data)

new_data = new_data.drop(["place"], axis = "columns")
print(new_data)

