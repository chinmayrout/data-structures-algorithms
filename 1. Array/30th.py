# Chocolate Distribution problem

# arr[0...n-1] represents sizes of packets m is number of students.
# Returns minimum difference between maximum and minimum values of distribution.

def findMinDiff(arr, n, m):
    # If there are no chocolates or number of studnets is 0
    if m == 0 or n == 0:
        return 0

    # Sort the given packets
    arr.sort()

    # Number of students cannot be more than the number of packets
    if n < m:
        return -1

    # Largest number of chocolates
    min_diff = arr[n - 1] - arr[0]

    # Find the subarray of size m such that difference between last(maximum in case of sorted) and
    # first (minimum in case of sorted) elements of subarray is minimum
    for i in range(n - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    
    return min_diff

# Driver Code
arr = [12, 4, 7, 9, 2, 23, 25, 41,
          30, 40, 28, 42, 30, 44, 48,
          43, 50]
m = 7 # Number of students
n = len(arr)
print("Minimum difference is", findMinDiff(arr, n, m))