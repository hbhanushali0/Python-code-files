



import matplotlib.pyplot as plt

months = ['june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']

mumbai = [82.5, 83.06, 83.61, 85.06, 90.75, 85.24, 84.06]

plt.plot(months, mumbai, linewidth = 3, marker = "o", markersize = 10, label = "Mumbai")
plt.title("Petrol Prices")
plt.xlabel("Months")
plt.ylabel("Prices")
plt.grid()
plt.legend(loc = "upper right", shadow = True)


plt.savefig('petrol prices.png')


plt.show()




