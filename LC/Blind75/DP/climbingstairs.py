# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n:int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one


# Driver Code
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))