
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


data = pd.read_csv("Mall_Customers.csv")
print(data.head())

print(data.isnull().sum())

# initial scatter

plt.scatter(data["Annual_Income"], data["Spending_Score"])
plt.show()

# features

features = data[["Annual_Income", "Spending_Score"]]

scaler = MinMaxScaler()
new_features = scaler.fit_transform(features)

print(features.head())
print(pd.DataFrame(new_features).head())

model = KMeans(n_clusters = 5)
result = model.fit_predict(new_features)
data["clusters"] = result
print(data.head())

plt.scatter(data["Annual_Income"], data["Spending_Score"], c = data["clusters"])
plt.xlabel("Annual_Income")
plt.ylabel("Spending_Score")
plt.show()





