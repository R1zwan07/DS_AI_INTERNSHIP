import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Day-13/Pattern_finder/housing_data_task3.csv")

print("\nDataset Preview:\n")
print(df.head())

corr_matrix = df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()

print("\nHighly Correlated Feature Pairs (> 0.8):\n")

high_corr_found = False

for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_value = corr_matrix.iloc[i, j]
        if abs(corr_value) > 0.8:
            print(f"{corr_matrix.columns[i]}  <-->  {corr_matrix.columns[j]} : {corr_value:.2f}")
            high_corr_found = True

if not high_corr_found:
    print("No highly correlated features found")

plt.figure(figsize=(6,5))
sns.boxplot(y=df["Price"])
plt.title("Outlier Detection in Price")
plt.tight_layout()
plt.show()

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]

print("\nOutlier Rows (Using IQR Method):\n")
print(outliers)

print("\nWhy this matters:")
print("Highly correlated features cause multicollinearity in ML models.")
print("Outliers distort averages and reduce prediction accuracy.")
