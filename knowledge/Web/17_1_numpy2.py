import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(np.vstack([A, B]))
print(np.hstack([A, B]))
print(A.reshape(9, 1)) # you cannot this: A.reshape(2, 5)
matrix = np.arange(1, 10)
print(matrix)
print("*"*10)

"""
Just like with range(), np.arange() starts with the first argument and
ends just before the second argument. So, np.arange(1, 10) returns an
array containing the numbers 1 through 9.

"""

print(np.arange(1, 10).reshape(3, 3))
print("*"*10)
np.arange(1, 13).reshape(3, 2, 2) # !!! ciekae dla mnie
print(np.arange(1, 24, 2).reshape(3, 2, 2))
print(np.random.random([3, 3]))





























