# Find if there is a subarray with 0 sum

def subArrayExists(arr):
    # Traverse through array and store prefix suns
    n_sums = 0
    s = set()
    n = len(arr)

    for i in range(n):
        n_sum += arr[i]
        
        # If prefix sum is 0 or it is already present
        if n_sum == 0 or n_sum in s:
            return True

        s.add(n_sum)

    return False


# Driver Code
arr = [-3, 2, 3, 1, 6]
print(subArrayExists(arr))