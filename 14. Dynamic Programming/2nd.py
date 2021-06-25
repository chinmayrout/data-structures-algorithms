# Knapsack Problem
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/


# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]        # making the DP array

    for i in range(1, n+1):         # taking the first i elements
        for w in range(W, 0, -1):   # starting from back, so that we also have data of previous
                                    # computation when taking i - 1 items
            if wt[i-1] <= w:
                # Finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i - 1])
    return dp[W]

# Driver Code
val = [1000, 100, 120]
wt = [10, 30, 20]
W = 50
n = len(val)

print(knapSack(W, wt, val, n))


# Time Complexity: O(N*W). As redundant calculations of states are avoided.

# Auxiliary Space: O(W) As we are using 1-D array instead of 2-D array.