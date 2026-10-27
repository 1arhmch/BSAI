import numpy as np
A = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

rows, cols = A.shape

for i in range(rows):
    for j in range(cols):
        print(A[i, j])