import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("Day-14/car_data.csv")

feature = df[["Salary"]]

std_scaler = StandardScaler()
salary_std = std_scaler.fit_transform(feature)

minmax_scaler = MinMaxScaler()
salary_norm = minmax_scaler.fit_transform(feature)

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.hist(feature, bins=6)
plt.title("Original Salary")

plt.subplot(1,3,2)
plt.hist(salary_std, bins=6)
plt.title("Standardized")

plt.subplot(1,3,3)
plt.hist(salary_norm, bins=6)
plt.title("Normalized")

plt.tight_layout()
plt.show()

print("\nWhy Scaling Matters:")
print("Distance-based algorithms (KNN/SVM) depend on magnitude. Scaling prevents Salary dominating Age.")
