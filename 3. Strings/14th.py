# Edit Distance
# https://www.geeksforgeeks.org/edit-distance-dp-5/

# Python3 Program to find minimum number of operations to convert str1 to str2
def editDist(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    # Create a DP array to memoize result previous computations
    DP = [[0 for i in range(n1 + 1)] for j in range(2)]

    # Base condition when second string is empty then we remove all characters
    for i in range(0, n1 + 1):
        DP[0][i] = i

    # Start filling the DP. This loop runs for every character in second string
    for i in range(1, n2 + 1):
        # This loop compares the char from second string with first string characters
        for j in range(0, n1 +1):
            # If first string is empty then we have to perform add character operations to get second string
            if (j==0):
                DP[i % 2][j] = i
            # IF character from both String is same, then we don't perform any operation. Here i % 2 is for bound the row number
            elif str1[j - 1] == str2[i - 1]:
                DP[i % 2][j] = DP[(i -1) % 2][j - 1]

            # If character from both string is not same, then we take the minimum from three specified opertaion
            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) %2][j], min(DP[i%2][j-1], DP[(i - 1)% 2][j - 1])))


    # After complete fill the DP array, if n2 is even, we end up in the 0th row else we end up in the 1st row, so we take
    # n2 % 2 to get row

    print(DP[n2 % 2][n1], "")



# Driver Code
str1 = "food"
str2 = "money"

editDist(str1, str2)