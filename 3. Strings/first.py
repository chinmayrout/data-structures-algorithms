#Reverse a String

def revString(a):

    b = ""
    
    for i in a:
        b = i + b   #adding the string into a new string one character at a time

    return b

def recursiveStringReversal(str):
    if len(str) == 0:
        return str
    else:
        return recursiveStringReversal(str[1:])+ str[0]


a = "How are you!"
print(revString(a))
print(recursiveStringReversal(a))