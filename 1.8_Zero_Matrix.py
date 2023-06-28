# Write an algorithm such that if an element in an 
# M x N matrix is 0, its entire row and column are set to 0

import numpy as np

def set_zeros(x, y, matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        matrix[i][x] = 0

    for i in range(cols):
        matrix[y][i] = 0

def find_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    arr = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                arr.append(i)
                arr.append(j)

    for i in range(len(arr)-1):
        set_zeros(arr[i], arr[i+1], matrix)
        i += 1

matrix = [[1,1,0,1],
          [1,1,1,1],
          [0,1,1,1]]

print('Matrix before transformation:')
print(np.matrix(matrix))
find_zeros(matrix)
print('Matrix after transformation:')
print(np.matrix(matrix))