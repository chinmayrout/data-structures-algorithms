class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid

            # Left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))

