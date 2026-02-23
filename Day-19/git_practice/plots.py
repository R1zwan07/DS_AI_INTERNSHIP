import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.plot(x, y)
plt.title("Visualization inside Feature Branch")
plt.xlabel("X values")
plt.ylabel("cos(x)")
plt.show()