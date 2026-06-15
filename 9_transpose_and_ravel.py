import numpy as np
# Create a 1D array
arr1D = np.arange(10)
print("1D Array:")
print(arr1D)

# Create a 2D array
arr2D = np.arange(12).reshape(3,4)
print("\n2D Array:")
print(arr2D)

# Create a 3D array
arr3D = np.arange(27).reshape(3,3,3)
print("\n3D Array:")
print(arr3D)

# Transpose of 2D array
print("\nTranspose of 2D array:")
print(arr2D.T)
# Transpose of 3D array
print("\nTranspose of 3D array:")
print(arr3D)
print(arr3D.T)

# Ravel of 2D array
print("\nRavel of 2D array:")
print(arr2D.ravel())
# Ravel of 3D array
print("\nRavel of 3D array:")
print(arr3D.ravel())
