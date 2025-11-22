import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
v = np.array([10, 20, 30])
x = np.array([1,5,10])
arr = np.array([10,20,30,40])
c = 5 
mat = np.array([
    [1,2,3],
    [4,5,6]
])

square_root = np.sqrt(a)
exp = np.exp(a)
logarithm = np.log(a)
sin = np.sin(a)
absolute = np.abs(a)
print(a + b)   # [11 22 33]
print(a - b)   # [-9 -18 -27]
print(a * b)   # [10 40 90]
print(b / a)   # [10. 10. 10.]
print(a + c)   # NumPy expands c → [5,5,5] internally.
print(mat + v) # NumPy replicated v across rows.


print(square_root)
print(exp)
print(logarithm)
print(sin)
print(absolute)

print(x > 4)     # [False True True]
print(x == 10)   # [False False True]

print(arr.sum())        # 100
print(arr.mean())       # 25
print(arr.min())
print(arr.max())
print(arr.std())        # standard deviation
print(arr.var())        # variance


print(mat.sum(axis=0))   # column-wise → [5 7 9]
print(mat.sum(axis=1))   # row-wise → [6 15]

