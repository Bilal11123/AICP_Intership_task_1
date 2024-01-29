import numpy as np

# Create a 5x5 array with random values
random_array = np.random.rand(5, 5)

# Print the resulting array
print("5x5 Array with Random Values:")
print(random_array)

# Find the minimum and maximum values in the array
minimum_value = np.min(random_array)
maximum_value = np.max(random_array)

# Print the minimum and maximum values
print("\nMinimum Value:", minimum_value)
print("Maximum Value:", maximum_value)
