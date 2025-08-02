
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

data = pd.read_csv("result_data.csv")
print(data)
print(data.isnull().sum())

feature = data[["hr"]]
target = data["result"]

model = DecisionTreeClassifier()
abc = model.fit(feature,target)

hr = float(input("enter hours "))
d = [[hr]]
print(model.predict(d))

text_tree = export_text(model)
print(text_tree)



plot_tree(abc, fontsize = 10, filled = True, feature_names = data.columns, class_names = ["F", "P"])

plt.show()



