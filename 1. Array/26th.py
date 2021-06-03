'''
In daily share trading, a buyer buys shares in the morning and sells them on the same day. 
If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction
 can only start after the first one is complete (Sell->buy->sell->buy). 
 Given stock prices throughout the day, find out the maximum profit that a share trader could have made.
'''

# Maximum profit by buying and selling a share at most twice
# Similiar to 17th.py

# Valley-Peak approach i.e. take a variable profit and initialize it with zero and then traverse through the array of price[] from (i+1)th position whenever the initial position value is greater than the previous value add it to variable profit.


def maxProfit(prices):
    n = len(prices)

    profit = 0  # initialize profit variable
    # Using Valley-Peak Approach
    '''
                           80
                           /
            30            /
           /  \          25
          /    15       /
         /      \      /
        2        10   /
                   \ /
                    8
    '''

    i = 1
    for i in range(n):
        sub = prices[i] - prices[i-1]
        if sub > 0:
            profit += sub


    print(profit)


price = [2, 30, 15, 10, 8, 25, 80]
maxProfit(price)


