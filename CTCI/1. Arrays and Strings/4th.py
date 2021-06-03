'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
1.5
1.6
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
'''

# Determine whether or not a string is a permutation of a palindrome
# Ignoring Spaces
# Understanding left

def isPalindromePermutation(string):
    counter = Counter()

    for letter in string.replace(' ', ''):
        counter[letter] += 1
    # Return sum([count % 2 for count in counter.values()]) < 2

    odd_counts = 0
    for count in counter.values():
        odd_counts += count % 2
        if odd_counts > 1:
            return False
    return True

class Counter(dict):
    def __missing__(self, key):
        return 0

print(isPalindromePermutation('aab'))
print(isPalindromePermutation('abc'))
