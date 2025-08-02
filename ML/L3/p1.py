# check for null


import pandas as pd

data = pd.read_csv("data.csv")
print(data)

# check for null data
res = data.isnull().sum()
print(res)

# find out age null values
d1 = data[data.Age.isnull()]
print(d1)

# find out position null values
d2 = data[data.Position.isnull()]
print(d2)

# if any value is null
d3 = data[data.isnull().any(axis = 1)]
print(d3)


