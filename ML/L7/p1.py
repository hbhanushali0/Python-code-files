
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("vehicle_data.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["Age"]]
target = data["Vehicle"]

model = LogisticRegression()
model.fit(feature,target)

age = float(input("enter age "))
print(model.predict([[age]]))

print(model.predict_proba([[age]]))

res = model.predict_proba([[age]]).ravel().tolist() # ravel - 2D numpy into 1d numpy # list - numpy array into list

print(res)

print("bike = ", round(res[0],2)*100, "car = ", round(res[1],2)*100, "cycle = ", round(res[2],2)*100)




