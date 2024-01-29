import numpy as np

def compute_statistics(array):
    mean = np.mean(array, axis=1)
    std_dev = np.std(array, axis=1)
    variance = np.var(array, axis=1)
    
    return mean, std_dev, variance

# Example usage:
# Create a 3x4 array with random values
example_array = np.random.rand(3, 4)

# Compute statistics using the function
mean_values, std_dev_values, variance_values = compute_statistics(example_array)

# Print the results
print("Array:")
print(example_array)
print("\nMean along the second axis:", mean_values)
print("Standard Deviation along the second axis:", std_dev_values)
print("Variance along the second axis:", variance_values)
