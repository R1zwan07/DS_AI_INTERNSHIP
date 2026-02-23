# Simple Bill Splitter

bill_amount = float(input("Enter the total bill amount: ₹"))

num_people = int(input("Enter the number of people: "))

share = bill_amount / num_people

print(f"\nTotal Bill: ₹{bill_amount}. Each person pays: ₹{share:.2f}")

