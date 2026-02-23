import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))

subject_means = scores.mean(axis=0)

centered_scores = scores - subject_means

print("Original Scores (5 Students x 3 Subjects):\n")
print(scores)

print("\nSubject-wise Mean Scores:\n")
print(subject_means)

print("\nCentered (Normalized) Scores:\n")
print(centered_scores)
