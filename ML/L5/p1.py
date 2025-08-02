# scatter plot


import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("pos_salary.csv")
print(data)

plt.scatter(data[["Level"]], data[["Salary"]])
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Level vs Salary")
plt.show()

