
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut, cross_val_score


data = pd.read_csv("salary_data-1.csv")
print(data)
print(data.isnull().sum())

feature = data[["Level"]]
target = data["Salary"]


x_train, x_test, y_train, y_test = train_test_split(feature,target, random_state = 101)

model = DecisionTreeRegressor()
model.fit(x_train,y_train)

sc1 = model.score(x_test,y_test)
print("Hold Out Score = ", sc1)



