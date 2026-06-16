import numpy as np

# np.sort
# Return a sorted copy of an array.

array1 = np.random.randint(1,100,15)
print("Original Array:")
print(array1)
print("\nSorted Array:")
sorted_array1 = np.sort(array1)
print(sorted_array1)

# along an axis
array2 = np.random.randint(1,100,(3,4))
print("\nOriginal 2D Array:")
print(array2)
print("\nSorted 2D Array along axis 0 (columns):")
sorted_array2_axis0 = np.sort(array2, axis=0)
print(sorted_array2_axis0)
print("\nSorted 2D Array along axis 1 (rows):")
sorted_array2_axis1 = np.sort(array2, axis=1)
print(sorted_array2_axis1)

# np.append
# The numpy.append() appends values along the mentioned axis at the end of the array

print("\nAppending values to a 1D array:")
array3 = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(array3)
appended_array3 = np.append(array3, [6, 7, 8])
print("Array after appending values:")
print(appended_array3)

# np.concatenate
# numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

arr1 = np.array([10 , 20 , 30])
arr2 = np.array([40 , 50 , 60])

# To concatenate two arrays
arr1_arr2 = np.concatenate((arr1 , arr2))
print(arr1_arr2)

# 2d array concatenation
arr2D_1 = np.array([[1 , 2] , [3 , 4]])
arr2D_2 = np.array([[5 , 6] , [7 , 8]])

arr2D_concatenate = np.concatenate((arr2D_1 , arr2D_2))
print("concatenate along the default axis (axis=0):\n", arr2D_concatenate)

arr2D_concatenate_axis0 = np.concatenate((arr2D_1 , arr2D_2) , axis=0) # concatenate along the rows
print("concatenate along axis 0:\n", arr2D_concatenate_axis0)

arr2D_concatenate_axis1 = np.concatenate((arr2D_1 , arr2D_2) , axis=1) # concatenate along the columns
print("concatenate along axis 1:\n", arr2D_concatenate_axis1)

# np.unique
# The numpy.unique() function finds the unique elements of an array.

array4 = np.array([1, 2, 3, 4, 5, 1, 2, 3])
print("Unique elements in the array: ", np.unique(array4))


# np.expand_dims
# The numpy.expand_dims() function expands the shape of an array.

array5 = np.arange(10)
array5_exp_a0 = np.expand_dims(array5 , axis=0) # expand along the first axis (rows)
print("Original Array shape: ", array5.shape)
print("Expanded Array shape axis 0: ", array5_exp_a0.shape)
array5_exp_a1 = np.expand_dims(array5 , axis=1) # expand along the second axis (columns)
print("Expanded Array shape axis 1: ", array5_exp_a1.shape)


# np.where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.

array6 = np.array([1, 2, 3, 4, 5])
indices = np.where(array6 > 3)
print("Indices where elements are greater than 3: ", indices)
print("Elements where condition is satisfied: ", array6[indices])

# conditional replacement
array7 = np.array([1, 2, 3, 4, 5])
replaced_array7 = np.where(array7 > 3, array7 * 10, array7) # replace elements greater than 3 with their value multiplied by 10
print("Array after conditional replacement: ", replaced_array7)


# np.histogram
# The numpy.histogram() function computes the histogram of a set of data.

data = np.array([76, 98, 99, 39,
       91, 46, 88, 23,
       45,  6, 83,  1,
       37, 43, 78, 85,
       54, 73, 61, 53,
       40, 93, 85, 77])

hist = np.histogram(data, bins=[0,10,20,30,40,50,60,70,80,90,100]) # compute histogram with 11 bins
print("Histogram:", hist)


# np.corrcoef
# The numpy.corrcoef() function returns the Pearson product-moment correlation coefficients.
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 1, 4, 2, 6])
correlation_matrix = np.corrcoef(x, y)
print("Correlation matrix:\n", correlation_matrix)

# np.isin
# The numpy.isin() function tests whether each element of an array is also present in a second array.
data = np.array([76, 98, 99, 39,
       91, 46, 88, 23,
       45,  6, 83,  1,
       37, 43, 78, 85,
       54, 73, 61, 53,
       40, 93, 85, 77])

values_to_check = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
isin_result = np.isin(data, values_to_check)
print("isin result:\n", isin_result)

# np.flip
# The numpy.flip() function reverses the order of elements in an array along the specified axis.
array8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:\n", array8)
flipped_array8 = np.flip(array8, axis=0) # flip along the first axis (rows)
print("Flipped Array along axis 0:\n", flipped_array8)
flipped_array8_axis1 = np.flip(array8, axis=1) # flip along the second axis (columns)
print("Flipped Array along axis 1:\n", flipped_array8_axis1)
print("Flipped Array along both axes:\n", np.flip(array8)) # flip along both axes


# np.put
# The numpy.put() function changes the value of specified elements in an array.

array9 = np.array([1, 2, 3, 4, 5])
print("Original Array:\n", array9)
np.put(array9, [0, 2], [10, 30]) # change the value of elements at indices 0 and 2 to 10 and 30 respectively
print("Array after using np.put:\n", array9)


# np.delete
# The numpy.delete() function returns a new array with sub-arrays along an axis deleted.
array10 = np.array([1, 2, 3, 4, 5])
print("Original Array:\n", array10)
deleted_array10 = np.delete(array10, [0, 2]) # delete elements at indices 0 and 2
print("Array after using np.delete:\n", deleted_array10)

