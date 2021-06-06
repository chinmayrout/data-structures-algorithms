# Print all the permutations of the given string

def toString(List):
    return ''.join(List)

def permute(s, start, end):
    if start == end:
        print(toString(s))
    
    else:
        for i in range(start, end+1):
            s[start], s[i] = s[i], s[start]
            permute(s, start + 1, end)
            s[start], s[i] = s[i], s[start]     # Using Backtracking

# Driver Code
s = "ABC"
n = len(s)
a = list(s)
permute(a, 0, n-1)

'''
1. The total number of permutation of a string formed by N characters(all distinct) is N!
2. The Total number of permutation of a string formed by N characters (where the frequency of character C1 is M1, C2 is M2… and so the frequency of character Ck is Mk) is N!/(M1! * M2! *….Mk!).
3. The total number of permutation of a string formed by N characters(all distinct) after fixing the first character is (N-1)!
'''
