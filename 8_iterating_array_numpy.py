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


# Iteration on 1D Array
print("\nIterating over 1D array:")
for i in arr1D:
    print(i)

# Iteration on 2D Array
print("\nIterating over 2D array:")
for j in arr2D:
    print(j)

# Iteration on 3D Array
print("\nIterating over 3D array:")
for k in arr3D:
    print(k)

# To iterate over single elements
for i in np.nditer(arr3D):
    print(i)