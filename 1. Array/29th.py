# Trapping Rain water problem

# Python Program to find maximum amount of water than can be trapped within given set of bar
# pending understand
def findWater(arr):
    n = len(arr)

    # Initialize output
    result = 0

    # Maximum element on left and right
    left_max = 0
    right_max = 0

    #Indices to traverse the array
    low = 0
    high = n - 1
    
    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                # Update max in left
                left_max = arr[low]
            else:
                # Water on curr element = max - curr
                result += left_max - arr[low]
            low += 1

        else:
            if arr[high] > right_max:
                # Update right maximum
                right_max = arr[high]
            else:
                result += right_max - arr[high]
            high -= 1
    return result

# Driver Code
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Maximum water that can be accumulated is ", findWater(arr))
print("Maximum water that can be accumulated is ", findWater(arr1))
