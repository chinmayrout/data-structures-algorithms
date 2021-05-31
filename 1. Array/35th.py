# Median of 2 sorted arrays of equal size
# This method works by first getting medians of the two sorted arrays and then comparing them.

# Using divide and conquer we divide the 2 arrays accordingly recursively till we get two elements in each array,
# hence we calculate median

#condition len(arr1) = len(arr2) = n

def getMedian(arr1, arr2, n):

    # If there is no element in any array
    if n == 0:
        return -1

    # 1 element in each => median of sorted arr made of two arrays will
    elif n == 1:
        # be sum of both elements by 2
        return (arr1[0] + arr[0]) / 2

    # eg; [1,4] , [6,10] => [1, 4, 6, 10]
    # median = (6+4) / 2
    elif n == 2:
        # which implies median = (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

    else:
        # Calculating Medians
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        # then the elements at median position must be between the greater median and the first element of respective arrays
        # and between the other median and last element in it's respective array
        if m1 > m2:
            if n % 2 == 0:
                return getMedian(arr1[:int(n / 2)+1], arr2[int(n/2)-1:], int(n/2)+1)
            else:
                return getMedian(arr1[:int(n/2)+1], arr2[int(n/2):], int(n/2)+1)

        else:
            if n % 2 == 0:
                return getMedian(arr1[int(n/2 - 1):], arr2[:int(n/2)+1], int(n/2)+1)

            else:
                return getMedian(arr1[int(n/2):], arr2[0:int(n/2)+1], int(n/2) +1)


# Function ot find median of arrays
def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n/2)] + arr[int(n/2)-1])/2

    else:
        return arr[int(n/2)]


# Driver Code:
arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]

n = len(arr1)
print(int(getMedian(arr1, arr2, n)))



'''

1) Calculate the medians m1 and m2 of the input arrays ar1[] 
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one 
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one    
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays 
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get 
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
'''
