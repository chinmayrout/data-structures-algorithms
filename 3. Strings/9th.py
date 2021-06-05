# Find Longest Recurring Subsequence in String
# https://www.geeksforgeeks.org/longest-repeating-subsequence/
# https://leetcode.com/problems/longest-repeating-substring/solution/

def search(L, a, modulus, n, nums):
    '''
    Rabin-Karp with polynomial rolling hash.
    Search a substring of given length that occurs at least 2 times.
    @return start position if the substring exits and -1 and otherwise
    '''

    # Compute the hash of the string S[:L]
    h = 0
    for i in range(L):
        h = (h * a + nums[i]) % modulus
    
    # Already seen hashes of strings of length L
    seen = {h}

    # Const value to be used ofter: a**L % modulus
    aL = pow(a, L, modulus)
    for start in range(1, n - L + 1):
        # Compute rolling hash in O(1) time
        h = (h * a - nums[start] - 1 * al + )

