import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)

income = np.random.exponential(scale=50000, size=1000)

scores = 100 - np.random.exponential(scale=15, size=1000)
scores = np.clip(scores, 0, 100)

datasets = {
    "Heights (Normal)": heights,
    "Income (Right Skewed)": income,
    "Scores (Left Skewed)": scores
}

for title, data in datasets.items():
    mean = np.mean(data)
    median = np.median(data)

    plt.figure(figsize=(6,4))
    sns.histplot(data, kde=True)
    plt.title(title)
    plt.axvline(mean, color='red', label=f"Mean={mean:.1f}")
    plt.axvline(median, color='green', label=f"Median={median:.1f}")
    plt.legend()
    plt.show()

    if mean > median:
        print(f"{title}: Right Skewed")
    elif mean < median:
        print(f"{title}: Left Skewed")
    else:
        print(f"{title}: Normal Distribution")
