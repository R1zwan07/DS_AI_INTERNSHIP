import numpy as np

data = np.arange(24)

reshaped_data = data.reshape(4, 3, 2)

transposed_data = reshaped_data.transpose(0, 2, 1)

print("Final Shape:", transposed_data.shape)
print("\nFinal Transposed Array:\n")
print(transposed_data)
