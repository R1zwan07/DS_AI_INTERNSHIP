# Simple Profile Card 

item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
in_stock_input = input("Is it in stock? (yes/no): ")

print("Item:", item_name, ",", "Qty:", quantity, ",", "Price:", price, ",", "Available:", in_stock_input)

total_cost = quantity * price
print("Total Cost:", total_cost)