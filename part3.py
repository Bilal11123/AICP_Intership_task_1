import numpy as np

# Define two matrices (2D arrays)
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Compute the cross product along axis 0 (default)
cross_product = np.cross(matrix1, matrix2)

# Print the resulting cross product matrix
print("Cross Product Matrix:")
print(cross_product)
