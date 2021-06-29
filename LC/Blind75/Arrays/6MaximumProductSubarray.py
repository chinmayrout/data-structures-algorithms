class Solution:
    def maxProduct(self, nums):
        n = len(nums)

        # Variables to store maximum and minimum product till ith index
        minVal = nums[0]
        maxVal = nums[0]

        maxProduct = nums[0]

        for i in range(1, n):
            # When multipliled by -ve number, maxVal becomes minVal and minVal becomes maxVal
            if nums[i] < 0:
                maxVal, minVal = minVal, maxVal

            # maxVal and minVal stores the product of subarray ending at nums[i]
            maxVal = max(nums[i], maxVal * nums[i])
            minVal = max(nums[i], minVal * nums[i])

            # MaxProduct of array
            maxProduct = max(maxProduct, maxVal)

        return maxProduct


# Driver Solution
s = Solution()
nums = [2,3,-2,4]
print(s.maxProduct(nums))