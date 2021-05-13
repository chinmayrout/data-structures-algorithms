#Write a Code to check whether one string is a rotation of another

#Using Count

def isRotation(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    temp = ''

    #chceck if sizes of two strings are same
    if size1 != size2:
        return False

    #Create a temp string with value str1.str1
    temp = str1 + str1

    #Now check if str2 is a substring of temp
    #string.count returns the number of occurrences of 
    #the second string in temp

    if(temp.count(str2) > 0):
        return True
    else:
        return False

#Driver Code
string1 = "AACD"
string2 = "ACDA"

if(isRotation(string1, string2)):
    print("Strings are rotations of each other")
else:
    print("False")

#can be done using KMP Algo