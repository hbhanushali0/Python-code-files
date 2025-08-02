# drop missing data - dropna 

import pandas as pd


data = pd.read_csv("data.csv")
print(data)

d1 = data.dropna(how = "any", axis = 0)
print(d1)

d2 = data.dropna(how = "all", axis = 0)
print(d2)

d3 = data.dropna(thresh = 3, axis = 0)
print(d3)

d4 = data.dropna(subset = ["Age"])
print(d4)

d5 = data.dropna(subset = ["Salary"])
print(d5)

d6 = data.dropna(subset = ["Age", "Salary"])
print(d6)




