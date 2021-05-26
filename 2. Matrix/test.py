# Spirally traversing a matrix
# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

# Python3 program to print given matrix in Spiral Form

#Simple Approach

def spirtalPrint(rowEnd, columnEnd, a):
    rowStart = 0
    columnStart = 0

    while(rowStart < rowEnd and columnStart <columnEnd):
        #Print the first row from the remaining rows

        for i in range(columnStart, columnEnd):
            print(a[rowStart][i], end = " ")
        rowStart+=1

        # Print the last column from the remaining columns
        for i in range(rowStart, rowEnd):
            print(a[i][columnEnd-1], end = " ")

        columnEnd -=1

        #Print the last row from the remaining rows
        if rowStart < rowEnd:
            for i in range(columnEnd-1, (columnStart- 1), -1):
                print(a[rowEnd - 1][i], end = " ")

            rowEnd-=1

        #Print the first column from the remaining columns
        if columnStart<columnEnd :
            for i in range(rowEnd-1, rowStart-1, -1):
                print(a[i][columnStart], end = " ")

            columnStart += 1

#Driver Code
a = [[1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13, 14, 15, 16,17, 18]]

R = 3
C = 6

spirtalPrint(R, C, a)