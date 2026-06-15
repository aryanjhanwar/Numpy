# Stacking -> Joining -> Concatenating -> Merging
# Splitting -> Dividing -> Slicing

# Stacking is the process of joining arrays along a new axis. 
# It is used to combine multiple arrays into a single array. 
# Two common stackings are horizontal stacking (hstack) and vertical stacking (vstack).
# The most common stacking functions in NumPy are np.stack(), np.hstack(), and np.vstack().
import numpy as np

array1 = np.arange(12).reshape(3,4)
array2 = np.arange(12, 24).reshape(3,4)

print("\nHorizontal Stacking:")
print(np.hstack([array1, array2 , array1]))

print("\nVertical Stacking:")
print(np.vstack([array1, array2, array1]))

print("\nStacking along a new axis:")
print(np.stack([array1, array2, array1], axis=1))

# Splitting is the process of dividing an array into multiple sub-arrays.
# It is used to break down a large array into smaller arrays.
# The most common splitting functions in NumPy are np.split(), np.hsplit(), and np.vsplit().
# splitting should be done in such a way that the array can be split into equal parts, 
# otherwise it will throw an error.

print("\nHorizontal Splitting:")
print(np.hsplit(array1, 2))

print("\nVertical Splitting:")
print(np.vsplit(array1, 3))