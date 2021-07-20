# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Brute-Force Approach - Calculate the sum of every k-element contigous subarray of the given array 
# and divide the sum by 'k' to find average.

def find_avg_subarray_brute(arr, K):
    result = []
    for i in range(len(arr) - K + 1):   #think about this
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum/K)   # Calculate average
    
    return result

# Driver
result = find_avg_subarray_brute([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
print(str(result))

def find_avg_sliding(arr, K):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # Add the next element
        # Slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum/K)  # Calculate the average
            windowSum -= arr[windowStart]
            windowStart += 1

    return result
result1 = find_avg_sliding([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
print(str(result1))
