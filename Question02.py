import numpy as np
# Create 1D array of 20 random numbers
arr = np.random.randint(1, 51, 20)
print("Array:")
print(arr)
# Minimum value and index
print("Minimum value:", arr.min())
print("Index of Minimum:", arr.argmin())
# Maximum value and index
print("Maximum value:", arr.max())
print("Index of Maximum:", arr.argmax())
# Sum of all elements
print("Sum:", arr.sum())
# Mean 
print("Mean:", arr.mean())
# Standard Deviation
print("Standard Deviation:", arr.std())