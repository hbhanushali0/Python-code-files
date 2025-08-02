import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("abp1.csv")
print(data)

data[["area","bedrooms"]] = data["info"].str.split(",",expand=True)
print(data)

features = data[["area","bedrooms"]]
target = data["price"]

model = LinearRegression()
model.fit(features.values, target)

area = float(input("enter area "))
bedrooms = float(input("enter bedrooms "))

price = model.predict([[area,bedrooms]])
print(round(price[0],2),"crs")


