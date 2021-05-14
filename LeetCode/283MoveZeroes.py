# https://leetcode.com/problems/move-zeroes/

def rightShifter(nums):
    ctr = 0
    for i in range(0, len(nums)):
        if(nums[i]!=0):
            nums[ctr], nums[i] = nums[i], nums[ctr]
            ctr+=1
    return nums

def leftShifter(nums):  #TODO
    
    ctr = len(nums)
    for i in range(len(nums),0,-1):
        if nums[i] != 0:
            nums[ctr], nums[i] = nums[i], nums[ctr]
            ctr-=1
    return nums



numarr = [0,0,1,0,1,0,5,3]
numarr1 = [0,0,1,0,1,0,5,3]
print(rightShifter(numarr))
print(leftShifter(numarr1))
