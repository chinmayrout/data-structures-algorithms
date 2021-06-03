# Minimum no. of operations required to make an array palindrome

# Returns minimum number of count operations required to make arr[] palindrome
def findMinOps(arr):
    n = len(arr)
    ans = 0     # Initialize Result

    # Start from two corners
    i, j = 0, n - 1

    while i <= j:
        # If corner elements are same, problem reduces arr[i+1...j-1]
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        # If left element is greater, then we merge right two elements
        elif arr[i] > arr[j]:
            # Need to merge from tail.
            j -= 1
            arr[j] += arr[j+1]
            ans += 1

        # Else we merge left two elements
        else:
            i += 1
            arr[i] += arr[i - 1]
            ans += 1

    return ans

# Driver Code
arr = [1, 4, 5, 9, 1]
print("Count of minimum no. of operations is:"+ str(findMinOps(arr)))