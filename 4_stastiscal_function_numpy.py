""""**Statistical Functions**
1. np.sum(a)
   -> Sum of all elements
 
2. np.mean(a)
   -> Average = Sum of elements / Number of elements
 
3. np.median(a)
   -> Middle value after sorting
 
4. np.min(a)
   -> Smallest value in array
 
5. np.max(a)
   -> Largest value in array
 
6. np.var(a)
   mean,difference,square,average | (sum = ddof) -> divide by array length
 
7. np.std(a)
   -> Standard Deviation = √Variance
   -> Measures spread of data
 
8. np.prod(a)
   -> Multiplication of all elements
 
9. np.cumsum(a)
   -> Cumulative (running) sum
 
10. np.cumprod(a)
    -> Cumulative (running) product
 
11. np.argmin(a)
    -> Index position of minimum value
 
12. np.argmax(a)
    -> Index position of maximum value
 
13. np.abs(a)
    -> Converts negative values to positive
    -> Absolute value (distance from zero)
 
14. np.unique(a)
    -> Returns unique values only
    -> Removes duplicates
 
15. np.percentile(a, 50)
    -> Finds percentage-based value
    -> 50th percentile = Median
 
16. np.quantile(a, 0.5)
    -> Similar to percentile
    -> 0.5 = 50%
 
17. np.ptp(a)
    -> Range = Max - Min
 
18. np.any(a)
    -> True if at least one value is True
 
np.sum(a) -> Sum of all elements
np.mean(a) -> Average = Sum of elements / Number of elements
np.median(a) -> Middle value after sorting
np.min(a) -> Smallest value in array
np.max(a) -> Largest value in array
np.var(a) mean,difference,square,average | (sum = ddof) -> divide by array length
np.std(a) -> Standard Deviation = √Variance -> Measures spread of data
np.prod(a) -> Multiplication of all elements
np.cumsum(a) -> Cumulative (running) sum
np.cumprod(a) -> Cumulative (running) product
np.argmin(a) -> Index position of minimum value
np.argmax(a) -> Index position of maximum value
np.abs(a) -> Converts negative values to positive -> Absolute value (distance from zero)
np.unique(a) -> Returns unique values only -> Removes duplicates
np.percentile(a, 50) -> Finds percentage-based value -> 50th percentile = Median
np.quantile(a, 0.5) -> Similar to percentile -> 0.5 = 50%
np.ptp(a) -> Range = Max - Min
np.any(a) -> True if at least one value is True
"""


# Statistical Functions in NumPy
import numpy as np

array1 = np.array([5 , 60 , 20 , 40 , 90 , 4])
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 1. To calculate the sum of an array
sum_array1 = np.sum(array1)
print("Sum of array1:", sum_array1)

# 2. To calculate the mean of an array
mean_array1 = np.mean(array1)
print("Mean of array1:", mean_array1)

# 3. To calculate the median of an array
median_array1 = np.median(array1)
print("Median of array1:", median_array1)

# 4. To calculate the minimum of an array
min_array1 = np.min(array1)
print("Minimum of array1:", min_array1)
min_array2_axis0 = np.min(array2 , axis=0) # minimum along axis 0 (columns)
print("Minimum of array2 along axis 0:", min_array2_axis0)
min_array2_axis1 = np.min(array2 , axis=1) # minimum along axis 1 (rows)
print("Minimum of array2 along axis 1:", min_array2_axis1)

# 5. To calculate the maximum of an array
max_array1 = np.max(array1)
print("Maximum of array1:", max_array1)

# 6. To calculate the variance of an array
var_array1 = np.var(array1)
print("Variance of array1:", var_array1)

# 7. To calculate the standard deviation of an array
std_array1 = np.std(array1)
print("Standard Deviation of array1:", std_array1)
max_array1 = np.max(array1)

print("Minimum of array1:", min_array1)
print("Maximum of array1:", max_array1)

# 8. To calculate the product of an array
prod_array1 = np.prod(array1)
print("Product of array1:", prod_array1)

# 9. To calculate the cumulative sum of an array
cumsum_array1 = np.cumsum(array1)
print("Cumulative sum of array1:", cumsum_array1)

# 10. To calculate the cumulative product of an array
cumprod_array1 = np.cumprod(array1)
print("Cumulative product of array1:", cumprod_array1)

# 11. To find the index of the minimum value in an array
argmin_array1 = np.argmin(array1)
print("Index of minimum value in array1:", argmin_array1)

# 12. To find the index of the maximum value in an array
argmax_array1 = np.argmax(array1)
print("Index of maximum value in array1:", argmax_array1)

# 13. To calculate the absolute value of an array
abs_array1 = np.abs(array1)
print("Absolute values of array1:", abs_array1)

# 14. To find the unique values in an array
unique_array1 = np.unique(array1)
print("Unique values in array1:", unique_array1)

# 15. To calculate the percentile of an array
percentile_25 = np.percentile(array1 , 25)
percentile_50 = np.percentile(array1 , 50)
percentile_75 = np.percentile(array1 , 75)
print("25th percentile of array1:", percentile_25)
print("50th percentile of array1:", percentile_50)
print("75th percentile of array1:", percentile_75)

# 16. To calculate the quantile of an array
quantile_25 = np.quantile(array1 , 0.25)
quantile_50 = np.quantile(array1 , 0.5)
quantile_75 = np.quantile(array1 , 0.75)
print("25th quantile of array1:", quantile_25)
print("50th quantile of array1:", quantile_50)
print("75th quantile of array1:", quantile_75)

# 17. To calculate the range of an array
range_array1 = np.ptp(array1)
print("Range of array1:", range_array1)

# 18. To check if any value in an array is greater than 50
any_greater_than_50 = np.any(array1 > 50)
print("Is any value in array1 greater than 50?", any_greater_than_50)
