
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("place_area_price.csv")
print(data)

features = data[["place", "area"]]
target = data[["price"]]

model = LinearRegression()
model.fit(features,target)

