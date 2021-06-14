# Find a specific pair in matrix
# https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/

# An efficient method to find maximum value of mat[d][c] - mat[a][b]
# such that c > a and d > b

import sys
N = 5

# The function returns maximym calue of A[c, d] - A[a, b] over all choices
# of indexes such that both c > a and d > b

def findMaxValue(mat):
    # Stores max value
    maxValue = -sys.maxsize - 1

    # maxArr[i][j] stores max of elements in matrix from (i, j) to (N -1, N-1)
    maxArr = [[0 for x in range(N)] for y in range(N)]

    # Last element of maxArr will be same as of the input matrix
    maxArr[N - 1][N - 1] = mat[N - 1][N - 1]

    # Pre-process last row
    maxV = mat[N - 1][N - 1]         # Initialize max
    for j in range(N - 2, -1, -1):
        if (mat[N - 1][j] > maxV):
            maxV = mat[N - 1][j]
        maxArr[N - 1][j] = maxV

    # PreProcess last column
    maxV = mat[N - 1][N - 1]        # Initialize max
    for i in range(N-2, -1, -1):
        if(mat[i][N - 1] > maxV):
            maxV = mat[i][N - 1]
        maxArr[i][N - 1] = maxV


    # Preprocess the rest of the matrix from bottom
    for i in range(N - 2, -1, -1):
        
