#Reverse the array

#Iterative Python program to reverse an array
#Function to reverse A[] from start to end

def reverseArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -=1

#Recursive Python Program to reverse an array
#Function to reverse A[] from start to end

def reverseArray1(A, start, end):
    if(start >= end):
        return
    
    A[start], A[end] = A[end], A[start]
    reverseArray1(A, start+1, end-1)

#Using Python Slicing
def reverseArray2(A):
    print(A[::-1])

# Driver Code to test all the functions

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseArray1(A, 0, 5)
print("Reversed List is:")
print(A)
print("Recursive Approach:")
reverseArray1(A, 0, 5)
print("Reversing Recurisively to the Old Way:")
print(A)
print("Using Python Slicing!")
reverseArray2(A)
