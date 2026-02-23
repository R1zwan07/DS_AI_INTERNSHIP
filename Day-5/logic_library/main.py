import math_operations

base = float(input("Enter base value: "))
exp = int(input("Enter exponent value: "))

power_result = math_operations.power(base, exp)
print(f"Power Result: {power_result}")

numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(float, numbers.split()))

average_result = math_operations.average(numbers_list)
print(f"Average: {average_result}")
