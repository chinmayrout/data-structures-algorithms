# Three way partitioning of an array around a given range
'''
Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts. 
1) All elements smaller than lowVal come first. 
2) All elements in range lowVal to highVVal come next. 
3) All elements greater than highVVal appear in the end. 
The individual elements of three sets can appear in any order.
'''
'''
An efficient solution is based on Dutch National Flag based QuickSort.
We traverse given array elements from left. 
We keep track of two pointers, first (called start in below code) to store next position of smaller element (smaller than range) from beginning;
and second (called end in below code) to store next position of greater element from end. 
'''

# Partitions arr[0...n-1] around [lowVal ... highVal]
def threeWayPartition(arr, lowVal, highVal):
    # Initialize ext available positions for smaller (than range) and greater elements
    n = len(arr)
    start = 0
    end = n - 1
    i = 0

    # Traverse elements from left
    while i <= end:
        # If current element is smaller than range, put it on next available smaller position
        if arr[i] < lowVal:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1

        # If current element is greater than range, put it on next available greater position
        elif arr[i] > highVal:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1

        else:
            i += 1


# Driver Code
arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
threeWayPartition(arr, 10, 20)
print(arr)