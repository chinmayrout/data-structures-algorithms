class Solution:
    def twosumII(self, nums, target):
        l, r = 0, len(nums) - 1

        while l < r:
            currSum = nums[l] + nums[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l +1, r +1]


# Driver Code
s = Solution()
numbers = [2,7,11,15]
target = 9
print(s.twosumII(numbers, target))