# Sigmoid function

import numpy as np

def sigmoid(array):
    return 1 / (1 + np.exp(-array))

# Example usage
input_array = np.array([-2, -1, 0, 1, 2])
output_array = sigmoid(input_array)

print("Input Array:")
print(input_array)
print("\nSigmoid Output Array:")
print(output_array)


# mean squared error function
actual = np.random.randint(1 , 50 , 25)
predicted = np.random.randint(1 , 50 , 25)

def meanSquareError(actual , predicted) :
    return np.mean((actual - predicted)**2)

errorArray = meanSquareError(actual , predicted)
print(errorArray)


