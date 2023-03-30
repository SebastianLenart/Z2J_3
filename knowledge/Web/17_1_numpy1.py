import numpy as np

matrix = np.array([[1, 2, 3], [4, 55, 6], [7, 8, 9]])
print(2*matrix)
print(matrix[1][1]) # OR
print(matrix[1, 1]) # !!!
print("*"*10)
print(matrix.shape)
print(matrix.diagonal())
print(matrix.flatten())
print(matrix.transpose())
print(matrix.min()," ; ", matrix.max(), " ; ", matrix.mean(), " ; ", matrix.sum())
print("*"*10)

"""
NumPy arrays
can only hold objects of the same type (for instance, all numbers)
whereas Pythons lists can hold mixed types of objects.

"""
second_matrix = np.array([[5, 4, 3], [7, 6, 5], [9, 8, 7]])
print(second_matrix - matrix)






















