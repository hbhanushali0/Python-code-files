
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

data = pd.read_csv("place_area_price.csv")
print(data)

features = data[["place","area"]]
print(features)

ct = ColumnTransformer([("place", OneHotEncoder(),[0])], remainder = "passthrough")
new_features = ct.fit_transform(features)
print(new_features)

new_features = pd.DataFrame(new_features[:, 1:], columns = ["khandala","lonavala", "area"])
print(new_features)


