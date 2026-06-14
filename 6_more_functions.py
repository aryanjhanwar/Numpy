import numpy as np

# log and exponents
array1 = np.random.random((3,3))
array1 = np.round(array1*100)
print("Exponential of array1:")
exp_array1 = np.exp(array1)
print(exp_array1)

print("\nNatural logarithm of array1:")
log_array1 = np.log(array1)
print(log_array1)

# round/floor/ceil
print("\nRounded values of array1:")
round_array1 = np.round(array1)
print(round_array1)

print("\nFloor values of array1:")
floor_array1 = np.floor(array1)
print(floor_array1)

print("\nCeil values of array1:")
ceil_array1 = np.ceil(array1)
print(ceil_array1)

#dot product
array2 = np.random.random((3,3))
print("\nDot product of array1 and array2:")
dot_product = np.dot(array1, array2)
print(dot_product)

# missing values
array3 = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
print("\nArray with missing values:")
print(array3)


