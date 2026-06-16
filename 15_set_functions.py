# set functions in numpy
import numpy as np

# np.intersect1d
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])
intersection = np.intersect1d(array1, array2)
print("Intersection of array1 and array2:", intersection)

# np.union1d
union = np.union1d(array1, array2)
print("Union of array1 and array2:", union)

# np.setdiff1d
set_diff = np.setdiff1d(array1, array2)
print("Set difference of array1 and array2 (elements in array1 not in array2):", set_diff)
set_diff_reverse = np.setdiff1d(array2, array1)
print("Set difference of array2 and array1 (elements in array2 not in array1):", set_diff_reverse)

# np.setxor1d
set_xor = np.setxor1d(array1, array2)
print("Symmetric difference of array1 and array2 (elements in either array1 or array2 but not in both):", set_xor)

# np.in1d
# array3 = np.array([2, 4, 6])
# in_array1 = np.in1d(array3, array1)
# print("Elements of array3 that are in array1:", in_array1)

# np.clip
array4 = np.array([1, 5, 10, 15, 20])
clipped_array4 = np.clip(array4, a_min=5, a_max=15)
print("Clipped array4 (values less than 5 set to 5 and values greater than 15 set to 15):", clipped_array4)