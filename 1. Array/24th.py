# Python program to find longest contigous subsequence

def findLongestConseqSubsq(arr):
    n = len(arr)

    s = set()       # Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements, we use the set() function without any argument.
    ans = 0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)

    # Check each possible sequence from last then update optimal length
    for i in range(n):
        # If current element is the starting element of a sequence
        if (arr[i] - 1) not in s:
            # Then check for next elements in the sequence
            j = arr[i]
            while j in s:
                j+=1

            # Update optimal length if this length is more
            ans = max(ans, j - arr[i])
    return ans


# Driver Code
if __name__=='__main__':
    arr = [1, 9, 3, 10, 4, 20, 2]
    print(findLongestConseqSubsq(arr))