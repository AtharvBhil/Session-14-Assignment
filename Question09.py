import numpy as np
arr = np.random.randn(6,6)
print("Matrix:")
print(arr)
# Properties
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
# Index of maximum value
print("Maximum Index:", np.argmax(arr))
# Index of minimum value
print("Minimum Index:", np.argmin(arr))
# Top-left 3x3 matrix
print("Top Left 3x3:", arr[0:3,0:3])
# replace all negative values with positive values
arr = np.abs(arr)
# Mean after modification
print("Mean:", arr.mean())