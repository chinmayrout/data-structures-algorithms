# Python program to find the row with maximum number of 1s

# Function that returns index of row with maximum number of 1s
def rowWithMax1s(matrix):
    # Initialize max values
    R = len(matrix)
    C = len(matrix[0])

    max_row_index = 0
    index = C - 1

    # Traverse for each row and count number os 1s by finding the index of 1s by 
    # finding the index of first 1
    for i in range(0, R):
        if index >= 0 and matrix[i][index] == 1:
            index -= 1
            max_row_index = i
    if max_row_index == 0 and matrix[0][C - 1] ==0:
        return 0
    return max_row_index

# Driver Code
matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

print("Index of Row with maximum 1s is:", rowWithMax1s(matrix))

