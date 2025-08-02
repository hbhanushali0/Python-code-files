
import pandas as pd
import matplotlib.pyplot as plt





data = pd.read_csv("salary_1.csv")
print(data)

plt.scatter(data.exp, data.salary, marker = "*", color = "blue")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Exp Vs Salary")
plt.show()







