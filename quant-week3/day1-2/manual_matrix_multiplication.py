import numpy as np

def manual_matmul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Incompatible matrix dimensions")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):          # row of A
        for j in range(cols_B):      # column of B
            for k in range(cols_A):  # iterate shared dimension
                result[i][j] += A[i][k] * B[k][j]
    
    return result

a = [[1,2,3],
     [4,5,6]]

b = [[7,8],
     [9,10],
     [11,12]]



A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[7,8],
              [9,10],
              [11,12]])

C = A @ B
c = np.dot(A,B)
print(C)
print(c)
print(manual_matmul(a, b))
