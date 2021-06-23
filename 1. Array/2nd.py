#Maximum and minimum of an array using minimum number of comparisons
# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Simple Linear Search
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


# Initialize values of min and max as minimum and maximum of the first two elements respectively.
# Starting from 3rd, compare each element with max and min, and change max and min accordingly
def getMinMax(arr: list) -> pair:
    minmax = pair()
    n = len(arr)
    # If there is only one element then return it as min and max both

    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]

    #if there are more than one element, then initialize min and max

    if(arr[0] > arr[1]):
        minmax.max = arr[0]
        minmax.min = arr[1]

    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



# Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.
def tournamentMinMax(low, high, arr):  # divide n conquer

    arr_max = arr[low]
    arr_min = arr[low]

    #if there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)

    #if there are only two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]

        return (arr_max, arr_min)       #check indentation of return statement

    #if there are more than 2 elements
    else:
        mid = int((low + high)/2)
        arr_max1, arr_min1 = tournamentMinMax(low, mid, arr)
        arr_max2, arr_min2 = tournamentMinMax(mid+1, high, arr)

        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
def compPairs(arr):     # Best method

    n = len(arr)
    #if array has even elements then initialize the first two elements as minimum and maximum

    if(n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])

        #set the starting index for loop
        i = 2

    #if array has odd number of elements then initialize the first element as minimum and maximum
    else:
        mx = mn = arr[0]

        #set the starting index of loop
        i = 1

        #In the while loop, pick elements in pair and compare the pair with the min and max so far
        while(i < n-1):
            if arr[i] < arr[i+1]:
                mx = max(mx, arr[i+1])
                mn = min(mn, arr[i])
            else:
                mx = max(mx, arr[i])
                mn = min(mn, arr[i+1])

            #increment the index by 2 as two
            #elements are processed in a loop
            i += 2

        return (mx, mn)


#Driver Code
if __name__ == '__main__':
    arr = [100, 32, 56, 1, -1, 200, 5]
    arr_size = len(arr)
    low = 0
    high = arr_size - 1
    minmax = getMinMax(arr)
    print("Maximum element is:", minmax.max)
    print("Minimum element is:", minmax.min)

    arr1 = [432, 112, 34, 2, 13, 55, 6]
    print(arr1)
    arr_maxz, arr_minz = tournamentMinMax(low, high, arr1)
    print(arr_maxz)
    print(arr_minz)
    mx, mn = compPairs(arr)  # using compare pairs method
    print(mx, mn)
