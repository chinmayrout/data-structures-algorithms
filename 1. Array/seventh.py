# Program to cyclically rotate an array by one

# Following are steps. 
# 1) Store last element in a variable say x. 
# 2) Shift all elements one position ahead. 
# 3) Replace first element of array with x.


#Python3 code for program to cyclically rotate an array by one

def rotate(arr):
    n = len(arr)
    x = arr[n - 1]

    for i in range(n-1, 0, -1):     #increment the sequence by -1; 1 is default
        arr[i] = arr[i-1]

    arr[0] = x

#Driver function
arr = [1,2,3,4,5,6]

print("Given Array is:", arr)

rotate(arr)

print("Rotated Array is:", arr)
