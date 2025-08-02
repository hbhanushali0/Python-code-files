

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

data = pd.read_csv("run_data.csv")
print(data)
print(data.isnull().sum())

features = data[["Weather","Just Ate"]]
target = data["Will I Go Running?"]

new_features = pd.get_dummies(features, drop_first = True)
print(new_features)

model = DecisionTreeClassifier()
abc = model.fit(new_features,target)


we = int(input("0 rainy 1 sunny "))
ja = int(input("0 no  1 yes "))
d = [[we,ja]]
print(model.predict(d))


text_tree = export_text(model)
print(text_tree)

plt.figure(figsize= (10,10))

plot_tree(abc, fontsize = 20 , feature_names = ["Weather","Just Ate"], filled = True, class_names = ["NO", "YES"])

plt.savefig("run_data.png")
plt.show()

