# Find Longest Recurring Subsequence in String
# https://www.geeksforgeeks.org/longest-repeating-subsequence/
# https://leetcode.com/problems/longest-repeating-substring/solution/


# Python3 program to find the longest repeating subsequence using recursion

# this function mainly returns LCS(str, str) with a confition that same characters at same index are not connected

def findLongestRepeatingSubSeq(X, m, n):
    if dp[m][n] != -1:
        return dp[m][n]

    # Return if we have reached the end of either string
    if m == 0 or n == 0:
        dp[m][n] = 0
        return dp[m][n]

    # If characters at index m and n mathces and index is different
    if X[m-1] == X[n-1] and m != n:
        dp[m][n] = findLongestRepeatingSubSeq(X, m-1, n-1) + 1

        return dp[m][n]

    # Else if characters at index m and n don't match
    dp[m][n] = max(findLongestRepeatingSubSeq(X, m, n-1), findLongestRepeatingSubSeq(X, m-1, n))

    return dp[m][n]

#Driver Code
str = "aabb"
m = len(str)
dp = [[-1 for i in range(1000)] for j in range(1000)]

print("The length of largest subsequence that repeats itself is:",findLongestRepeatingSubSeq(str, m, m))