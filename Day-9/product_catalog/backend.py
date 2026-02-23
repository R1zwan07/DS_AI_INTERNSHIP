import pandas as pd

products = pd.Series(
    data=[700, 150, 300],
    index=["Laptop", "Mouse", "Keyboard"]
)

laptop_price = products["Laptop"]

first_two_products = products[:2]

print("Full Products Series:\n")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Indexing):\n")
print(first_two_products)
