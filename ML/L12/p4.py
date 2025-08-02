
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

data = pd.read_csv("titanic_data.csv")
print(data.head())
print(data.shape)

data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis = "columns", inplace = True)

print(data.isnull().sum())

data.fillna({"Embarked": "S"}, inplace = True)
data.fillna({"Age": data["Age"].mean()}, inplace = True)

print(data.isnull().sum())

features = data.drop("Survived", axis = "columns")
target = data["Survived"]

print(features.head())
print(target.head())


new_features = pd.get_dummies(features, drop_first = True)
print(new_features.head())

x_train, x_test, y_train, y_test = train_test_split(new_features, target,random_state = 33)

model = DecisionTreeClassifier()
abc = model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(y_test)
print(y_pred)


cr = classification_report(y_test, y_pred)
print(cr)


d = [[3,22.0,1,0,7.25,1,0,1]]
print(model.predict(d))

tree = export_text(model)
print(tree)

plot_tree(abc, fontsize = 2, filled = True, feature_names = data.columns, class_names = ["0", "1"])
plt.show()






