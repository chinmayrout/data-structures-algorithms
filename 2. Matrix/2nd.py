# Search an element in a matrix
# https://leetcode.com/problems/search-a-2d-matrix/solution/


def findRow(matrix, k):    # k is the element to be searched
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])


    # binary Search
    left, right = 0, m * n -1
    while left <= right:
        pivot_idx = (left + right) // 2
        pivot_element = matrix[pivot_idx // n][pivot_idx % n]
        if k == pivot_element:
            return True
        else:
            if k < pivot_element:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

    return False

# Driver Code
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
k  = 3
print(findRow(matrix, k))