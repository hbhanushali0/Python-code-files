
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("home_prices_1.csv")
print(data)

area = data["area"].tolist()
price = data["price"].tolist()

print(area)
print(data)

plt.scatter(area,price,marker = "*",color = "red")
plt.xlabel("area")
plt.ylabel("prices")
plt.title("Lonavala prices")
plt.show()


