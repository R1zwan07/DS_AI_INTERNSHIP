import numpy as np
import pandas as pd

np.random.seed(0)
salary = np.random.normal(50000, 8000, 100)

salary = np.append(salary, [150000, 170000, 200000])

df = pd.DataFrame({"Salary": salary})

mean = df["Salary"].mean()
std = df["Salary"].std()

df["z_score"] = (df["Salary"] - mean) / std

outliers = df[abs(df["z_score"]) > 3]

print("Mean:", mean)
print("Standard Deviation:", std)

print("\nOutliers Detected:")
print(outliers)
