
P_heads = 1/2
P_six = 1/6

P_both = P_heads * P_six

print("Independent Events:")
print("P(Heads AND 6) =", P_both)

P_first_red = 5/10
P_second_red = 4/9

P_both_red = P_first_red * P_second_red

print("\nDependent Events:")
print("P(Both Red without replacement) =", P_both_red)

print("\nWhy denominator changed?")
print("Because after removing one red marble, total marbles reduced from 10 to 9")
