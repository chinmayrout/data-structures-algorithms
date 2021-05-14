#Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]

#Brute-Force Approach
#===========================================================================================

def printSubStr(str, low, high):

    for i in range(low, high+1):
        print(str[i], end = "")

#This funciton prints the longest substring.
#It also returns the length of the longest palindrome
def longestPalSubst(str):
    #Get the length of input String
    n = len(str)

    #All subStrings of length 1 are palindromes
    maxLength = 1
    start = 0

    #Nested loop to mark start and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1

            #Check Palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0

            #Palindrome
            if(flag != 0 and (j - i +1) > maxLength):
                start = i
                maxLength = j - i + 1

    print("Longest palindrome substring is: ",  end = "")
    printSubStr(str, start, start + maxLength - 1)

    #Return Length of LPS
    return maxLength

#Driver Code
if __name__ == '__main__':
    str = "asasmmalayalamm"
    print("\nLength is: ", longestPalSubst(str))


#===========================================================================================
#Dynamic Approach: https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/

def longestPalStr(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0

    #One by one consider every character as center point of even and length palindrome
    for i in range(1, length):

        #Find the longest even length palindrom with center points as i-1 and i.
        low  = i - 1
        high = i
        
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low +1
            low -= 1
            high += 1

        #Find the longest odd length palindrome with center point as i
        low = i - 1
        high = i + 1
        while low>=0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        
    print("Longest palindrome substring is:", string[start:start+maxLength])
    return maxLength

#Driver Code:
string1 = "mamalayalamamanac"
print(longestPalStr(string1))
#===========================================================================================