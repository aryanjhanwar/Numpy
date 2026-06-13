import numpy as np

a1 = np.arange(12).reshape(3,4)
print(a1)

a2 = np.arange(12,24).reshape(3,4)
print(a2)

# scalar operations

# scalar addition
print("\nScalar addition in a1:")
a3 = a1 + 10
print(a3)

# scalar subtraction
print("\nScalar subtraction in a1:")
a4 = a1 - 5
print(a4)

# scalar multiplication
print("\nScalar multiplication in a1:")
a5 = a1 * 2
print(a5)

# scalar division
print("\nScalar division in a1:")
a6 = a1 / 2
print(a6)

# scalar exponentiation
print("\nScalar exponentiation in a1:")
a7 = a1 ** 2
print(a7)


# Relational operations
print("\nRelational operations:")
print(a1 > 5) # element-wise comparison, returns a boolean array

# Logical operations
print("\nLogical operations:")
print((a1 > 5) & (a1 < 10)) # element-wise logical AND
print((a1 < 5) | (a1 > 10)) # element-wise logical OR
print(~(a1 > 5)) # element-wise logical NOT

# vectorized operations
print("\nVectorized operations:")
print("a1 + a2: \n", a1 + a2) # element-wise addition
print("a1 - a2: \n", a1 - a2) # element-wise subtraction
print("a1 * a2: \n", a1 * a2) # element-wise multiplication
print("a1 / a2: \n", a1 / a2) # element-wise division
print("a1 ** a2: \n", a1 ** a2) # element-wise exponentiation


