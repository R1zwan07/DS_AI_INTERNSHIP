import pandas as pd

# Sample dataset simulating the problem
data = {
    "Price": ["$1200", "$850", "$430", "$999"],
    "Date": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-20"]
}

df = pd.DataFrame(data)

print("Initial Data Types:\n")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData Types After Conversion:\n")
print(df.dtypes)

print("\nCleaned DataFrame:\n")
print(df)
