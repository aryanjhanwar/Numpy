# numpy arrays are more efficient than lists in terms of memory and performance.
# numpy arrays are homogeneous, which means that all elements in the array must be of the same data type.
# lists can contain elements of different data types.

import numpy as np

# Comparing the speed of numpy arrays and lists for a simple operation like addition.

print("Speed for lists : ")
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time 

start = time.time()
for i in range(len(a)):
  c.append(a[i] + b[i])
print(time.time()-start)

start = time.time()
print("\nSpeed for numpy arrays : ")
a = np.arange(10000000)
b = np.arange(10000000,20000000)
c = a + b
print(time.time()-start)


# Comparing the memory usage of numpy arrays and lists.
import sys
print("\nMemory usage for lists : ")
a = [i for i in range(10000000)]
print(sys.getsizeof(a))

print("\nMemory usage for numpy arrays : ")
a = np.arange(10000000)
print(sys.getsizeof(a))

