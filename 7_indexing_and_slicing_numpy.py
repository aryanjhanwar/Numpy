# indexing -> accessing individual elements of an array

# slicing -> accessing a range of elements in an array

import numpy as np
# Create a 1D array
arr1D = np.arange(12)
print("1D Array:")
print(arr1D)

# Create a 2D array
arr2D = np.arange(12).reshape(3,4)
print("\n2D Array:")
print(arr2D)

# Create a 3D array
arr3D = np.arange(8).reshape(2,2,2)
print("\n3D Array:")
print(arr3D)
# in 2d and 3d just tell me the element to acess dont need to give me the answer in print 

# accessing individual elements in 1D array
print("\nAccessing individual elements in 1D array:")
print("Element at index 5:", arr1D[5])

# accessing individual elements in 2D array
print("\nAccessing individual elements in 2D array:")
print("Accessing the element 9:", arr2D[2,1])

# accessing individual elements in 3D array
print("\nAccessing individual elements in 3D array:")
print("Accessing the element 3:", arr3D[0 , 1 , 1])


# slicing

# 1D array slicing
print("\nSlicing in 1D array:")
print("Elements from index 2 to 5:", arr1D[2:6])

# 2D array slicing
print("\nSlicing in 2D array:")
print("Slicing the first two rows and last two columns:")
print(arr2D[:2 , 2:])

# 3D array slicing
print("\nSlicing in 3D array:")
print("Slicing the first block and all rows and columns:")
print(arr3D[0 , : , :])

print("\nSlicing the 1 , 3 , 5 , 7:")
print(arr3D[: , : , 1])

print("\nSlicing the 0 , 3 , 8 , 11 in 2D array:")
print(arr2D[::2 , ::3])

print("\n Slicing the 1  3, 9 ,11 in 2D array:")
print(arr2D[::2 , 1::2])
print(arr2D[0:2: , 1::])

arr3D2 = np.arange(27).reshape(3,3,3)
print("\n3D Array 2:")
print(arr3D2)

print(arr3D2[::2 , 0:1:2 , ::2])