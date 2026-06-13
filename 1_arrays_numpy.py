import numpy as np

# Create a 1D array
arr1D = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1D)
print(type(arr1D))

# Create a 2D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2D)
print(type(arr2D))

# Create a 3D array

arr3D = np.array([[[1 , 2] , [3 , 4]] , [[4 , 5] , [6 , 7]]])
print("\n3D Array:")
print(arr3D)
print(type(arr3D))


# dtype
arr_int = np.array([1, 2, 3], dtype=int)
print("\nInteger Array:")
print(arr_int)

arr_float = np.array([1, 2, 3], dtype=float)
print("\nFloat Array:")
print(arr_float)


# zeros array
arr = np.zeros(10)
print(arr)

arr1 = np.zeros((3,4))
print(arr1)

# ones array
arr2 = np.ones(10)
print(arr2)
arr3 = np.ones((3,4))
print(arr3)

arrM = np.zeros((3 , 4)) + 10
print(arrM)

# full array
arr4 = np.full((3,4), 5)
print(arr4)


# Random array

#1D array with random values between 0 and 1
arrR1D = np.random.random(10)
print(arrR1D)


# 2D array with random values between 0 and 1
arrR2D = np.random.random((3 , 4))
print(arrR2D)

# linspace array
arrL = np.linspace(-10 , 10 , 5 , dtype=int) # start from -10, end at 10 and generate 5 equally spaced values 
print(arrL)

# identity array
arrI = np.identity(4) # 4x4 identity matrix
print(arrI)

# eye array
arrE = np.eye(4) # 4x4 identity matrix
print(arrE)

# diag array
arrD = np.diag([1, 2, 3, 4]) # diagonal array with 1, 2, 3, 4 on the diagonal
print(arrD)

# empty array
arrEm = np.empty((3,4)) # uninitialized array with random values
print(arrEm)

# array operations

arrO = np.arange(11).reshape(11,1)
print("shape:",np.shape(arrO))
print("dimension:", np.ndim(arrO))
print("size:",np.size(arrO))
print("data type:", arrO.dtype)