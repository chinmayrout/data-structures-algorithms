# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/
# https://www.geeksforgeeks.org/stock-buy-sell/

def maxProfit(prices):
    n = len(prices)
    cost = 0
    maxCost = 0

    if n == 0:
        return 0

    # Store the first element of array in a variable
    min_price = prices[0]

    for i in range(n):
        # Now compare first element with all the elements of array and find the minimum element
        min_price = min(min_price, prices[i])

        # Since min_price is smallest element of the array so subtract with every element of the array and return the maxCost
        cost = prices[i] - min_price

        maxCost = max(maxCost, cost)

    return maxCost

# Driver Code
prices = [7, 1, 5, 5, 6, 4]
print(maxProfit(prices))