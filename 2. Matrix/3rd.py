# Find median in row wise sorted matrix

from bisect import bisect_right as upper_bound

MAX = 100

# Function to find median in a matrix
def binaryMedian(matrix, row, col):
    mi = matrix[0][0]
    mx = 0
    for i in range(row):
        if matrix[i][0] < mi:
            mi = matrix[i][0]
        if matrix[i][col - 1] > mx:
            mx = matrix[i][col-1]
    desired = (row * col + 1) // 2

    while(mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0];

        # Find cound of elements smaller than mid
        for i in range(row):
            j = upper_bound(matrix[i], mid)
            place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1

        else:
            mx = mid
    print("Median is", mi)
    return

# Driver Code
row = 3
col = 3

matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
binaryMedian(matrix, row, col)




'''
Algorithm:  

1. First, we find the minimum and maximum elements in the matrix. The minimum element can be easily found by comparing the first element of each row, and similarly, the maximum element can be found by comparing the last element of each row.
2. Then we use binary search on our range of numbers from minimum to maximum, we find the mid of the min and max and get a count of numbers less than our mid. And accordingly change the min or max.
3. For a number to be median, there should be (r*c)/2 numbers smaller than that number. So for every number, we get the count of numbers less than that by using upper_bound() in each row of the matrix, if it is less than the required count, 
    the median must be greater than the selected number, else the median must be less than or equal to the selected number. 
'''