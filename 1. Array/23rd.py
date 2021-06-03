# find maximum product subarray 

# Function to find maximum product subarray
def maxProduct(arr):

    n = len(arr)

    # Variables to store maximum and minimum product till ith index
    minVal = arr[0]
    maxVal = arr[0]

    maxProduct = arr[0]

    for i in range(1, n):
        # When multiplied by -ve number, maxVal becomes minVal and minVal becomes maxVal
        if arr[i] < 0:
            maxVal, minVal = minVal, maxVal

        # MaxVal and minVal stores the product of subarray ending at arr[i]
        maxVal = max(arr[i], maxVal * arr[i])
        minVal = min(arr[i], minVal * arr[i])

        # Max Product of array
        maxProduct = max(maxProduct, maxVal)

    # Return maximum product found in array
    return maxProduct


# Driver Code
if __name__ == '__main__':
    arr = [-1, -3, -10, 0, 60]
    
    print("Maximum subarray product is", maxProduct(arr))




'''
The idea is to traverse array from left to right keeping two variables minVal and maxVal which represents 
the minimum and maximum product value till the ith index of the array. Now, if the ith element of the array
 is negative that means now the values of minVal and maxVal will be swapped as value of maxVal will become 
 minimum by multiplying it with a negative number. Now, compare the minVal and maxVal. 
The value of minVal and maxVal depends on the current index element or the product of the current index element and the previous minVal and maxVal respectively.

'''
