
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#load the dataset
boston_dataset = load_boston()
print(boston_dataset)

#check desc
print(boston_dataset.DESCR)

#check dataframe
boston = pd.DataFrame(boston_dataset.data, columns = boston_dataset.feature_names)

print(boston.head())

#check null
print(boston.isnull().sum())

# add price
boston["PRICE"] = boston_dataset.target
print(boston.head())

features = boston.drop(["PRICE"], axis = "columns")
target = boston[["PRICE"]]



x_train, x_test, y_train, y_test = train_test_split(features,target,random_state = 88)

model = LinearRegression()
model.fit(x_train,y_train)

train_score = model.score(x_train,y_train)
print("train_score = ", train_score)

test_score = model.score(x_test,y_test)
print("test_score =  ", test_score)


