
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score


data = pd.read_csv("dosage_eff_data.csv")
print(data)
print(data.isnull().sum())


feature = data[["dos"]]
target = data["eff"]

#holdout

x_train, x_test, y_train, y_test = train_test_split(feature,target)
m2 = DecisionTreeRegressor()
m2.fit(x_train, y_train)
sc1 = m2.score(x_test, y_test)
print("hold out ", sc1)

# KFold

kf = KFold(n_splits = 2, shuffle = True)
sc2 = cross_val_score(m2,feature,target,scoring = "r2", cv = kf)
print(sc2)


