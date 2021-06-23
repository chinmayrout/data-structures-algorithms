# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
def sol1(array):

    low = 0
    high = len(array) - 1
    mid = 0
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low = low + 1
            mid = mid + 1
        elif array[mid] == 1:
            mid = mid + 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    print(array)

def sol2(arr):
    cnt0 = 0    #all counters should be zero
    cnt1 = 0
    cnt2 = 0

    #Count the number of 0s, 1s and 2s in the array

    for i in range(len(arr)):
        if arr[i] == 0:
            cnt0+=1

        elif arr[i] == 1:
            cnt1+=1
        
        elif arr[i] == 2:
            cnt2+=1

    #Update the array
    i = 0

    #Store all the Os in the beginning
    while(cnt0 > 0):
        arr[i] = 0
        i+=1
        cnt0 -=1

    #Then all the 1s
    while(cnt1 > 0):
        arr[i] = 1
        i+=1
        cnt1-=1

    #Finally all the 2s
    while(cnt2 > 0):
        arr[i] = 2
        i+=1
        cnt2-=1

    print(arr)

#Driver Code
array = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
array1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sol1(array)
sol2(array1)
