

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, classification_report


data = pd.read_csv("loan_prediction.csv")
print(data.head())

# preprocessing
data.drop("Loan_ID", axis = "columns", inplace = True)
print(data.head())

res = data.isnull().sum()
print(res)

# fill null values
data.fillna({"Gender":"Male",
             "Married":"Yes",
             "Dependents":"0",
             "Self_Employed":"No",
             "LoanAmount":data["LoanAmount"].mean(),
             "Loan_Amount_Term":data["Loan_Amount_Term"].mean(),
             "Credit_History":1 },inplace = True)

res = data.isnull().sum()
print(res)
print(data.head())

# handling categorical data

cat_cols = ["Gender","Married","Education","Self_Employed","Property_Area","Dependents"]

df = pd.get_dummies(data[cat_cols])
print(df.head())

df = pd.get_dummies(data[cat_cols], drop_first = True)
print(df.head())

new_data = pd.concat([data, df], axis = "columns")
print(new_data.head())

new_data.drop(cat_cols, axis = "columns", inplace = True)
print(new_data.head())

features = new_data.drop(["Loan_Status"], axis = "columns")
target = new_data["Loan_Status"]

print(features)
print(target)

x_train, x_test, y_train, y_test = train_test_split(features,target)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
cr = classification_report(y_test, y_pred)
print(cr)

