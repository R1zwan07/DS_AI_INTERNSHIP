import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Day-13/Relationship_map/housing_data.csv")

print("\nDataset Preview:\n")
print(df.head())

plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df, color="blue")

plt.title("Relationship Between House Size and Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(x="City", y="Price", data=df, palette="Set2")

plt.title("Price Distribution Across Bangalore Areas")
plt.xlabel("Area")
plt.ylabel("Price")

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

correlation = df["SquareFootage"].corr(df["Price"])

print("\nObservation:")
if correlation > 0.4:
    print("As SquareFootage increases, Price generally increases.")
elif correlation < -0.4:
    print("As SquareFootage increases, Price generally decreases.")
else:
    print("SquareFootage has weak or no clear relationship with Price.")

print(f"Correlation Value: {correlation:.2f}")

print("\nWhy this matters:")
print("This helps decide whether SquareFootage is a useful feature for ML prediction.")
