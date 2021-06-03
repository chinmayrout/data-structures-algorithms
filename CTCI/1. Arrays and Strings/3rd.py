'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

# Basically we need to replace single spaces with %20 and remove trailing spaces

# Function to replace single spaces with %20 and remove trailing space
def urlify(string, length):
    new_index = len(string)
    string = list(string)
    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3

        else:
            # Move Characters
            string[new_index - 1] = string[i]
            new_index -=1

    return ''.join(string)


# Driver Code
test_string = 'Mr John Smith    '
length = 13
print(urlify(test_string, length))