import numpy as np

arr = np.array([10, 20, 30, 40])
mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
data = np.array([
    [1, 2, 3, 6],     # feature 1
    [2, 4, 6, 12],    # feature 2
    [10, 20, 30, 60]  # feature 3
])


mean = np.mean(arr)
c_mean = mat.mean(axis=0)    # column-wise mean → [2.5 3.5 4.5]
r_mean = mat.mean(axis=1)    # row-wise mean → [2. 5.]
s_deviation = np.std(arr)
variance = np.var(arr)
corr = np.corrcoef(data)
corr_column = np.corrcoef(data.T)

print(mean)
print(c_mean)
print(r_mean)
print(s_deviation)
print(variance)
print(corr)
print(corr_column)
