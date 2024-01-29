import numpy as np

# Define a square matrix (2D array)
matrix = np.array([[1, 2],
                   [3, 4]])

# Compute the determinant of the matrix
determinant = np.linalg.det(matrix)

# Print the resulting determinant
print("Determinant of the matrix:")
print(determinant)
