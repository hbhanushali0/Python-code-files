

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree



data = pd.read_csv("home_prices_data.csv")
print(data)
print(data.isnull().sum())

data.fillna({"area": data["area"].mean()}, inplace = True)
data.fillna({"price": data["price"].mean()}, inplace = True)

print(data)
print(data.isnull().sum())

feature = data[["area"]]
target = data["price"]

model = DecisionTreeRegressor()
abc = model.fit(feature,target)

a = float(input("enter area  "))
p = model.predict([[a]])
print("price = ", p)


tree = export_text(model)
print(tree)

plot_tree(abc, fontsize = 10, feature_names = data.columns, filled = True)
plt.show()



