# find common elements In 3 sorted arrays

def findCommon(arr1, arr2, arr3):

    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    val = []
    # Initialize starting indexex for ar1[], arr2[], arr3[]
    i, j, k = 0, 0, 0

    # Iteraye through three arrays while all arrays have elements
    while i < n1 and j < n2 and k < n3:

        # If x = y  and y = z, print any of them and move ahead in all arrays
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            val.append(arr1[i])
            i += 1
            j += 1
            k += 1

        # x < y
        elif arr1[i] < arr2[j]:
            i += 1
        
        # y < z
        elif arr2[j] < arr3[k]:
            j += 1

        # We reach here when x > y and z < y. i.e. z is smallest
        else:
            k += 1

    return val
    

# Driver Code to check the above function
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(*findCommon(ar1, ar2, ar3))