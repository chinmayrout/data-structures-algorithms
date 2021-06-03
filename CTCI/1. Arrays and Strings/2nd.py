# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = Counter()

    for c in str1:
        counter[c] += 1

    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


s1 = "acbd"
s2 = "bacd"
s3 = '3563476'
s4 = '7334566'
s5 = 'abcd'
s6 = 'd2cba'

print(check_permutation(s1, s2))
print(check_permutation(s3, s4))
print(check_permutation(s5, s6))
