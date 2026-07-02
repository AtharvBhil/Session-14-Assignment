import numpy as np
arr = np.random.randint(1, 101, (5,5))
print("Original Matrix:")
print(arr)
# Diagonal elements
print("\nDiagonal:")
print(np.diag(arr))
# Elements greater than 50
print("\nGreater than 50:")
print(arr[arr > 50])
# Replacing elements less than 30 with 0
arr[arr < 30] = 0
print("\nModified Matrix:")
print(arr)