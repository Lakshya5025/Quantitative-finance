import numpy as np


a = np.array([10, 20, 30, 40, 50, 60]) # Create a array of in which all elements are or number
b = np.array([[1,2,3],[4,5,6],[7,8,9]]) # create a 2-d array
zeros = np.zeros((2, 2)) # create a 2-d array of zeros of 2x2
ones = np.ones((2, 3))  # create a 2-d array of ones of 2x3
r = np.arange(0, 10, 2) # create a array of numbers from 0 to 10 with 2 gap 10 excluded
lin = np.linspace(0, 8, 5)  # create a array of numbers from 0 to 8 even gap, 5 elements
reshape_2x3 = a.reshape(2, 3)
reshape_3x2 = a.reshape(3, 2)
flat = b.flatten()      # returns new array
ravel = b.ravel()       # returns view (no copy)
transpose = b.T # Transpost of matrix
print(a)
print(b)
print(zeros)
print(ones)
print(r)
print(lin)

print(a[1:4])   # [20 30 40]
print(a[:3])    # [10 20 30]
print(a[::2])   # [10 30 50]

print(b[0, 1])      # element at row 0, col 1
print(b[0:2, 1:3])  # rows 0–1, cols 1–2 → [[2 3], [5 6]]
print(b[:, 0])      # all rows, col 0 → [1 4 7]

print(reshape_2x3)
print(reshape_3x2)

print(flat)
print(ravel)
print(transpose)