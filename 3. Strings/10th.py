#Print all subsequences of a string

# Using pick and don't pick concept

def printSubSequences(s1, subStr = ""):

    if len(s1) == 0:
        print(subStr, end = " ")
        return

    # We start adding 1st character in string
    printSubSequences(s1[:1], subStr + s1[-1])

    # Not adding first character of strign because the concept of subsequence either character will be present or not
    printSubSequences(s1[:-1], subStr)
    return


s = "abc"
printSubSequences(s)