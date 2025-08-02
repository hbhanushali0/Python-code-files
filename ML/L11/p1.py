

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree


data = pd.read_csv(("loan_default_data.csv"))
print(data)
print(data.isnull().sum())

features = data[["GENDER", "OCCUPATION"]]
target = data["DEFAULT"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

print(target)

model = DecisionTreeClassifier()
abc = model.fit(new_features,target)

gen = int(input("0 female , 1 male "))
occ = int(input("0 business , 1 salary "))
d = model.predict([[gen,occ]])
print(d)

# tree - textual

text_tree = export_text(model)
print(text_tree)

# tree - graphical

plt.figure(figsize = (10,10))
plot_tree(abc, fontsize = 20, feature_names = ["GENDER", "OCCUPATION"], filled = True, class_names = ["NOPE", "YEAHH"])

plt.savefig("loandata.png")
plt.show()


