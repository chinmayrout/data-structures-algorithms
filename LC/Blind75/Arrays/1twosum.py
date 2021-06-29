# https://leetcode.com/problems/two-sum/
# use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice;

def twoSum(nums, target):
    prevMap = {}    # Every Previous element would be stored in this
    # Val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]

        prevMap[n] = i

    return

arr = [2, 7, 11, 15]
tar = 9

print(twoSum(arr, tar))