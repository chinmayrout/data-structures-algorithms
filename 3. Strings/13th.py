# Word Wrap Problem
# https://www.geeksforgeeks.org/word-wrap-problem-space-optimized-solution/

import sys

def solveWordWrap(arr, k):
    n = len(arr)

    dp = [0] * n    # dp[i] represents minimum cost of the line in which arr[i] is the first word
    
    # Array in which ans[i] store index of last word in line starting with word arr[i]
    ans = [0] * n   # represents index of last word present in line in which word arr[i] is the first word.

    # If only one word is present, then only one line is required. Cost of last line is zero. Hence, cost of this line is zero.
    # Ending point is also n - 1 as single word is present

    dp[n-1] = 0
    ans[n-1] = n-1

    # Make each word first word of line by iterating over each index in arr.
    for i in range(n - 2, -1, -1):
        currlen = -1
        dp[i] = sys.maxsize

        # Keep on adding words in current line by iterating from starting word upto last word in arr
        for j in range(i, n):
            # Update number of characters in current line. arr[j] is number of characters in current word
            # and 1 represents space character between two words.
            currlen += (arr[j] + 1)

            #If limit of characters is violated then no more words can be added to current line
            if currlen > k:
                break

            # If current word that is added to line is last word of arr then current line is last line.
            # Cost of last line is 0. Esle cost is square of extra spaces plus cost of putting line breaks 
            # in rest of wors from j+1 to n-1

            if (j==n-1):
                cost = 0
            else:
                cost = ((k - currlen) * (k - currlen) + dp[j+1])

            # Check if this arrangement geives minimum cost for line starting with word arr[i]
            if cost < dp[i]:
                dp[i] = cost
                ans[i] = j

    # Print starting index and ending index of words present in each line
    i = 0
    while(i<n):
        print(i+1, ans[i] + 1, end = " ")
        i = ans[i] + 1


# Driver Code
arr = [3, 2, 2, 5]  # aaa bb cc ddddd
k = 6               # per line 6
solveWordWrap(arr, k)