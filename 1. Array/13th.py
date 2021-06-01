# Kedane Algorithm - same as quesiton 8
# https://leetcode.com/problems/maximum-subarray/solution/

def maxSubArray(nums):

    # Initialize our variables usign the first element
    current_subarray = max_subarray = nums[0]

    # Start witht the 2nd element since we already used the first one
    for num in nums[1:]:
        # If the current_subarray is negative, throw it away. Otherwise keep adding to it.
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))