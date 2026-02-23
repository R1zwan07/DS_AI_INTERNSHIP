import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

df = pd.read_csv("Day-13/Distribution_Deep-drive/housing_data.csv")

print("\nDataset Preview:\n")
print(df.head())

price = df["Price"]

price_skew = skew(price)
price_kurtosis = kurtosis(price)

print("\nStatistical Analysis of Price Column")
print("------------------------------------")
print(f"Skewness  : {price_skew:.3f}")
print(f"Kurtosis  : {price_kurtosis:.3f}")

plt.figure(figsize=(8,5))
sns.histplot(price, kde=True, bins=10, color="skyblue")

plt.title("Price Distribution (Histogram + KDE)")
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

if price_skew > 0:
    print("\nInterpretation: Data is Right-Skewed (High price outliers present)")
elif price_skew < 0:
    print("\nInterpretation: Data is Left-Skewed")
else:
    print("\nInterpretation: Data is Normally Distributed")

plt.figure(figsize=(12,6))
sns.countplot(x="City", data=df, palette="viridis")

plt.title("Bangalore Area Frequency Count")
plt.xlabel("Areas")
plt.ylabel("Number of Houses")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

most_common_city = df["City"].mode()[0]
print(f"\nMost frequent area (Mode): {most_common_city}")

print("\nWhy this matters:")
print("If price data is skewed -> Apply Log Transformation before ML models")
