friend_a = set()
n1 = int(input("How many interests does Friend A have? "))

for i in range(n1):
    interest = input("Enter an interest for Friend A: ")
    friend_a.add(interest)

friend_b = set()
n2 = int(input("\nHow many interests does Friend B have? "))

for i in range(n2):
    interest = input("Enter an interest for Friend B: ")
    friend_b.add(interest)

shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b

print("\nShared Interests:")
print(shared_interests)

print("\nAll Unique Interests:")
print(all_interests)

print("\nInterests only Friend A has:")
print(unique_to_a)

print("\nInterests only Friend B has:")
unique_to_b = friend_b - friend_a
print(unique_to_b)