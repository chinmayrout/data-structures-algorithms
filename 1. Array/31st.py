# Smallest Subarray with sum greater than a given value

# Returns length of smallest subarray with sum greater than x
# If there is no subarray with given sum, then return n+1

def smallestSubwihSum(arr, x):
    n = len(arr)

    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = n + 1

    # Initialize starting and ending indexes
    start = 0
    end = 0
    while end < n:
        # Keep adding array elements while current sum is smaller or equal to x
        while curr_sum <= x and end < n:
            curr_sum += arr[end]
            end += 1

        # If current sum becomes greater than x
        while