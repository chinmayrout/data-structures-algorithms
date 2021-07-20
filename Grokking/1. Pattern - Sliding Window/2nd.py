# Maximum sum of any contiguous subarray of size ‘k’.

# Brute Force
'''
A basic brute force solution will be to calculate the sum of all ‘k’ sized subarrays of the given array, to find the subarray with the highest sum. We can start from every index of the given array and add the next ‘k’ elements to find the sum of the subarray. 
'''
def max_sub_arry(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        
        max_sum = max(max_sum, window_sum)

    return max_sum

# Driver Code
arr = [2, 1, 5, 1, 3, 2]
print(max_sub_arry(arr, 3)) 

# Sliding Window
def max_sub_array_sliding(arr, k):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

# Driver Code
arr1 = [2, 1, 5, 1, 3, 2]
print(max_sub_array_sliding(arr, 3)) 