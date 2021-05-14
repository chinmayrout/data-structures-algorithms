#https://leetcode.com/problems/two-sum/


def twosum(nums: list[int], target: int):
    reqd = {}       #dictionary
    for i in range(len(nums)):
        if target - nums[i] in reqd:
            return [reqd[target - nums[i]], i]
        else:
            reqd[nums[i]] = i


input_list = [2,8,12,15]
print(twosum(input_list, 20))