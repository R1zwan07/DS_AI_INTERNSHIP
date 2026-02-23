import random

actions = ["Click", "Scroll", "Exit"]

sample_space = []

for a in actions:
    for b in actions:
        sample_space.append((a, b))

print("Sample Space:")
print(sample_space)
print("Total Outcomes:", len(sample_space))

event = [outcome for outcome in sample_space if "Click" in outcome]

probability_click = len(event) / len(sample_space)

print("\nEvent (At least one Click):")
print(event)
print("Probability:", probability_click)


trials = 1000
count_sum7 = 0

for _ in range(trials):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 + die2 == 7:
        count_sum7 += 1

experimental_probability = count_sum7 / trials

print("\nExperimental Probability of Sum = 7:", experimental_probability)
