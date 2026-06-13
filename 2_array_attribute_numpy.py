import numpy as np

# Create a 1D array
arr1D = np.arange(10 , dtype = np.int32) # vector 
print("1D Array:")
print(arr1D)

# Create a 2D array
arr2D = np.arange(12 , dtype = np.float64).reshape(3,4) # matrix
print("\n2D Array:")
print(arr2D)

# Create a 3D array
arr3D = np.arange(8, dtype = np.int64).reshape(2,2,2) # tensor
print("\n3D Array:")
print(arr3D)

#ndim attribute
print("\nndim attribute gives the number of dimensions of the array.")
print("Number of dimensions in 1D array:", arr1D.ndim)
print("Number of dimensions in 2D array:", arr2D.ndim)
print("Number of dimensions in 3D array:", arr3D.ndim)

# shape attribute
print("\n(shape) attribute gives the dimensions of the array as a tuple.")
print("Shape of 1D array:", arr1D.shape)
print("Shape of 2D array:", arr2D.shape)
print("Shape of 3D array:", arr3D.shape)

# size attribute -> total number of elements in the array
print("\n(size) attribute gives the total number of elements in the array.")
print("Size of 1D array:", arr1D.size)
print("Size of 2D array:", arr2D.size)
print("Size of 3D array:", arr3D.size)

# itemsize attribute -> size of each element in bytes
print("\n(itemsize) attribute gives the size of each element in bytes.")
print("Item size of 1D array:", arr1D.itemsize, "bytes")
print("Item size of 2D array:", arr2D.itemsize, "bytes")
print("Item size of 3D array:", arr3D.itemsize, "bytes")

# nbytes attribute -> total number of bytes consumed by the array
print("\n(nbytes) attribute gives the total number of bytes consumed by the array.")
print("Total bytes consumed by 1D array:", arr1D.nbytes, "bytes")
print("Total bytes consumed by 2D array:", arr2D.nbytes, "bytes")
print("Total bytes consumed by 3D array:", arr3D.nbytes, "bytes")

# dtype attribute -> data type of the elements in the array
print("\n(dtype) attribute gives the data type of the elements in the array.")
print("Data type of 1D array:", arr1D.dtype)
print("Data type of 2D array:", arr2D.dtype)
print("Data type of 3D array:", arr3D.dtype)

# astype() method -> to change the data type of the array
print("\n(astype) method is used to change the data type of the array.")
arr1D_float = arr1D.astype(np.float64)
print("1D array with float data type:")
print(arr1D_float)
arr2D_int = arr2D.astype(np.int32)
print("\n2D array with integer data type:")
print(arr2D_int)
arr3D_float = arr3D.astype(np.float32)
print("\n3D array with float data type:")
print(arr3D_float)