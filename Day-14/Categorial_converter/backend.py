import pandas as pd

df = pd.read_csv("Day-14/car_data.csv")

print("\nOriginal Data:\n", df.head())

df["Transmission"] = df["Transmission"].map({"Manual":0, "Automatic":1})

color_encoded = pd.get_dummies(df["Color"], prefix="Color", drop_first=True)

df = pd.concat([df.drop("Color", axis=1), color_encoded], axis=1)

print("\nEncoded Data:\n", df.head())

print("\nExplanation:")
print("Transmission is ordinal -> Label Encoding used")
print("Color is nominal -> One-Hot Encoding used with drop_first=True to avoid dummy variable trap")
