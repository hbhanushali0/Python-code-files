

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("insurance_data.csv")
print(data.head())

res = data.isnull().sum()
print(res)

plt.scatter(data["age"], data["have_insurance"])
plt.xlabel("age")
plt.ylabel("have insurance")
plt.show()


