# Python Program to print Factorial

# Recursive Approach
def recurFact(n):

    if n == 0:
        return 1

    if n == 1:
        return 1

    else:
        return n * recurFact(n-1)

# Driver Code
n = 5
print(recurFact(n))


# Iterative Approach
def iterFact(n):
    res = 1

    for i in range(2, n+1):
        res = res * i   # can also be written as res *= i
    return res

# Driver Code
n = 5
print(iterFact(n))