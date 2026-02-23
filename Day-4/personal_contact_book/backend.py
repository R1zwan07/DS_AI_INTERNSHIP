contacts = {}

n = int(input("How many contacts do you want to add initially? "))

for i in range(n):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

print("\nAdd or Update a Contact")
name = input("Enter name: ")
phone = input("Enter phone number: ")
contacts[name] = phone

print("\nSafe Lookup")
search_name = input("Enter name to search: ")
print("Result:", contacts.get(search_name, "Contact not found"))

search_name = input("Enter another name to search: ")
print("Result:", contacts.get(search_name, "Contact not found"))

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
