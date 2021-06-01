# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1   -   pending


# Function to use inversion count
def mergeSort(arr, n):
    # A temp_arr is created to store sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)

#This function will use MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):
    # A variable inv_count is used to store inversion counts in each recursive call
    inv_count = 0

    # We will make recursive call if and only if we have more than one elements
    if left < right:
        # mid is calculated to divide the arrat into two subarrays
        # Floor division is must in case of python
