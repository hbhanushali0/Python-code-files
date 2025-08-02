

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree

data = pd.read_csv("salary_data-1.csv")
print(data)

print(data.isnull().sum())

feature = data[["Level"]]
target = data["Salary"]

model = DecisionTreeRegressor()
abc = model.fit(feature,target)

l = int(input("enter level  "))
s = model.predict([[l]])
print("salary = ",s)

tree = export_text(model)
print(tree)

plot_tree(abc, feature_names = data.columns, filled = True)
plt.show()


