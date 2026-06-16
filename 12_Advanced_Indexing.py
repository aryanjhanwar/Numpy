# Fancy Indexing in Numpy

import numpy as np
# Create a 2D array
arr2D = np.arange(24).reshape(6,4)
print("2D Array:")
print(arr2D)


# Fancy Indexing
print("\nFancy Indexing:")
print("Accessing the rows 1, 4, and 5:")
print(arr2D[[1,4,5]])

print("\nAccessing the columns 0 , 2 and 3:")
print(arr2D[:, [0,2,3]])

# Boolean Indexing
print("\nBoolean Indexing:")
arr2D = np.array([[76, 98, 99, 39],
       [91, 46, 88, 23],
       [45,  6, 83,  1],
       [37, 43, 78, 85],
       [54, 73, 61, 53],
       [40, 93, 85, 77]])

print("find all numbers greater than 50:")
print(arr2D[arr2D > 50])

print("\nfind out even numbers:")
print(arr2D[arr2D % 2 == 0])

print("\nfind all numbers greater than 50 and are even:")
print(arr2D[(arr2D > 50) & (arr2D % 2 == 0)])

print("\nfind all numbers divisible by 7:")
print(arr2D[arr2D % 7 == 0])

print("\nfind all numbers not divisible by 7:")
print(arr2D[~(arr2D % 7 == 0)])

