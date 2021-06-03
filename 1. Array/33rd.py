# Minimum swaps required to bring all elements less than or equal to k together
# Python program to find minimum swaps required to club all elements less than or equal to k together

# Utility function to find minimum swaps required to club all elements less than or equal to k together
def minSwap(arr, k):
    # Find count of elements which are less than equal to k
    n = len(arr)
    count = 0
    for i in range(0, n):
        if arr[i] <= k:
            count += 1

    # Find unwanted elements in current window of size 'count'
    bad = 0
    for i in range(0, count):
        if arr[i] > k:
            bad = bad + 1

    # Initialize answer with 'bad' value of current window
    ans = bad
    j = count
    for i in range(0, n):
        if j == n:
            break

        # Decrement count of previous window
        if arr[i] > k:
            bad = bad - 1

        # Increment count of current window
        if arr[j] > k:
            bad = bad + 1

        # Update ans if count of 'bad' is less in current window
        ans = min(ans, bad)

        j = j + 1

    return ans


# Driver code
arr = [2, 1, 5, 6, 3]
k = 3
print (minSwap(arr, k))
  
arr1 = [2, 7, 9, 5, 8, 7, 4]
k = 5
print (minSwap(arr1, k))






'''
A simple approach is to use two pointer technique and sliding window.

Find count of all elements which are less than or equals to ‘k’. Let’s say the count is ‘cnt’
Using two pointer technique for window of length ‘cnt’, each time keep track of how many elements in this range are greater than ‘k’. Let’s say the total count is ‘bad’.
Repeat step 2, for every window of length ‘cnt’ and take minimum of count ‘bad’ among them. This will be the final answer.
'''

'''
Read Two Pointer Technique: https://www.geeksforgeeks.org/two-pointers-technique/
Window Sliding Technique: https://www.geeksforgeeks.org/window-sliding-technique/
'''
