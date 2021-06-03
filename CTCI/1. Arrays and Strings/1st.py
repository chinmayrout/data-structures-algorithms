# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def findUnique(s):
    # Assuming character set is ASCII (128 characters)

    if len(s)> 128:
        return False

    char_set = [False for _ in range(128)]
    for char in s:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


st = "MUYU"
st1 = "abcd"

print(findUnique(st))
print(findUnique(st1))