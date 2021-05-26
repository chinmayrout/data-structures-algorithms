#Kedane's Algorithm
# The simple idea of Kadane’s algorithm is to look for all positive 
# contiguous segments of the array (max_ending_here is used for this). 
# And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). 
# Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far 

def maxSubArraySum(arr):

    max_so_far = a[0]
    max_ending_here = 0
    # curr_max = a[0]
    size = len(arr)

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
        # curr_max = max(a[i], curr_max + a[i])
        # max_so_far = max(max_so_far, curr_max)

    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(a))