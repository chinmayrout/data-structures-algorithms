#Check whether a String is Palindrome or not

def isPalindrome(s):    #simple way
    s1 =""
    for i in s:
        s1 = i + s1

    if(s==s1):
        return True

def isPalindromeRecursive(s):
    s = s.lower()
    l = len(s)

    if l < 2:
        return True
    
    elif s[0] == s[l-1]:
        return isPalindromeRecursive(s[l: l - 1])

def isPalindr(s):

    for i in range(0, int(len(s)/2)):       #without using any extra space
        if s[i] != s[len(s) - i - 1]:
            return False

    return True

a = "malayalam"
print(isPalindrome(a))
print(isPalindromeRecursive(a)) 
ans = isPalindr(a)      #Another way of printing output

if (ans):
    print("Yes")

else:
    print("No")
