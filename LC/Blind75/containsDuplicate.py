# https://leetcode.com/problems/contains-duplicate
# hashset to get unique values in array, to check for duplicates easily
def containsDuplicate(arr):
    return len(arr) != len(set(arr))


# Driver Code
arr = [1, 5, 4, 1, 24, 5, 0]
arr1 = [1, 2, 3, 4, 5, 67, 7, 0]
print(containsDuplicate(arr))
print(containsDuplicate(arr1))
