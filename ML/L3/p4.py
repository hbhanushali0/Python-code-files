# filling missing values


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("data.csv")
print(data)

imp1 = SimpleImputer(missing_values = np.nan, strategy = "constant", fill_value = "bench")
data[["Position"]] = imp1.fit_transform(data[["Position"]])
print(data)



#imp2 = SimpleImputer(missing_values = np.nan, strategy = "most_frequent")
#data[["Position"]] = imp1.fit_transform(data[["Position"]])
#print(data)



#imp3 = SimpleImputer(missing_values = np.nan, strategy = "median")
#data[["Age"]] = imp3.fit_transform(data[["Age"]])
#print(data)


#data[["Experience"]] = imp3.fit_transform(data[["Experience"]])
#print(data)


#imp4 = SimpleImputer(missing_values = np.nan, strategy = "mean")
#data[["Age"]] = imp4.fit_transform(data[["Age"]])
#print(data)

#data[["Experience"]] = imp4.fit_transform(data[["Experience"]])
#print(data)
