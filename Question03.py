import numpy as np
# Create a 4x5 matrix
arr = np.random.randint(20, 81, (4, 5))
print("Matrix:")
print(arr)
# Overall statistics
print("Minimum value:", arr.min())
print("Maximum value:", arr.max())
print("Sum of all elements:", arr.sum())
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())
# Row-wise sum
print("Row-wise Sum:",arr.sum(axis=1))
# Column-wise sum
print("Column-wise Sum:",arr.sum(axis=0))
