

import pandas as pd


data = pd.read_csv("data.csv")
print(data)

d1 = data.fillna({"Age": data["Age"].mean()})
print(d1)

d2 = data.fillna({"Salary": data["Salary"].mean()})
print(d2)

d3 = data.fillna({"Experience": data["Experience"].mean()})
print(d3)

d4 = data.fillna({"Position": "Unallocated"})
print(d4)

d5 = data.fillna({"Salary": 10000,"Age": 21, "Position": "Unallocated" })
print(d5)

data.fillna({"Salary": data["Salary"].mean(), "Position":"Unallocated", "Age": data["Age"].mean()}, inplace = True)
print(data)




