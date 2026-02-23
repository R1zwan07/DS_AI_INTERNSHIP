# Unique Visitors Tracker using Sets

# Take raw login IDs from user
raw_logs = []
n = int(input("How many login IDs do you want to enter? "))

for i in range(n):
    user_id = input("Enter User ID: ")
    raw_logs.append(user_id)

# Convert list to set to remove duplicates
unique_users = set(raw_logs)

# Membership test
check_id = input("\nEnter a User ID to check presence: ")
print("Is user present:", check_id in unique_users)

# Count comparison
print("\nTotal login entries:", len(raw_logs))
print("Unique users:", len(unique_users))

# Display unique users
print("\nUnique User IDs:")
for user in unique_users:
    print(user)
