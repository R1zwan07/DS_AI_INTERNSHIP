import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)

file_path = os.path.join(BASE_DIR, "customer_orders.csv")

df = pd.read_csv(file_path)

print("DataFrame Shape Before Cleaning:")
print(df.shape)

print("\nMissing Values Report:")
print(df.isna().sum())

numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].median()
)

df_cleaned = df.drop_duplicates()

print("\nDataFrame Shape After Cleaning:")
print(df_cleaned.shape)
