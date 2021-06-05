# Find duplicate characters in a string

def findDuplicate(string):
    duplicates = {}
    for char in string:
        #checking whether char is already present in the dictionary or not

        if char in duplicates:
            #increasing count if present
            duplicates[char] += 1
        else:
            #initializing count to 1 if not present
            duplicates[char] = 1

    for key, value in duplicates.items():
        if value > 1:
            print(key, end = " ")
    print()

def findDuplicatePy(string):        #using python with string methods
    duplicates = []
    for char in string:
        if string.count(char) > 1:
        
            if char not in duplicates:
                duplicates.append(char)
    print(*duplicates)

s = input("Enter string to find duplicates in:")
findDuplicate(s)
findDuplicatePy(s)