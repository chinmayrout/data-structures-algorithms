# Split the Binary string into two substring with equal 0’s and 1’s
# https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/

#Function to return the count of maximum substrings str can be divided into
def maxSubStr(s):
    n = len(s)

    # To store the count of 0s and 1s
    count0 = 0
    count1 = 0

    # To store the count of maximum substrings s can be divided into
    cnt = 0
    for i in range(n):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

        if count0 == count1:
            cnt += 1

    # it is not possible to split the string
    if cnt == 0:
        return -1
    
    return cnt

# Driver Code
s = "0100110101"
print(maxSubStr(s))