


import matplotlib.pyplot as plt
import numpy as np



products = ['laptos', 'printer', 'router']
reena = [10, 25, 15]
veena = [5,30,12]

x = np.arange(len(products))
plt.bar(x, reena, width = 0.30, label = "reena")
plt.bar(x+0.30, veena, width = 0.30, label = "veena")
plt.xticks(x, products)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.title("Performance Analysis")
plt.savefig("performance.pdf")



plt.show()