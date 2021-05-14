#Write a Program to check whether a string is a valid shuffle of two strings or not
#AKA: Interleaving of two given strings with no common characters

#Returns true if C is interleaving of A and B, otherwise returns false

def isInterleaved(A, B, C):

    #Utility vartiables
    i = 0
    j = 0
    k = 0

    #Iterate through all characters of C

    while k != len(C) - 1:

        #Match first character of C with first character of A,
        #If matches then move A to next
        if i< len(A) and A[i] == C[k]:
            i+=1

        #Else match first character of C with first character of B
        #If matches then move B to next
        elif j < len(B) and B[j] == C[k]:
            j+=1

        #If doesn't match with either A or B, then return false
        else:
            return False
        
        #Move C to next for next iteration
        k+=1

    #If A or B still have some characters, then length of C is
    # smaller than sum of lengths of A and B, so return false
    if(i < len(A) or j < len(B)):
        return False

    return True

#Driver Code
A = "AB"
B = "CD"
C = "ACBD"
D = "ACBD"
E = "ADBC"
print(isInterleaved(A, B, C))
print(isInterleaved(A, B, D))
print(isInterleaved(A, B, E))