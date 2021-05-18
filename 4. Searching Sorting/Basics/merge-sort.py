# Python program for implementation of MergeSort

def mergeSort(array):
    if len(array) > 1:

        # Finding the mid of the array
        mid = len(array) // 2     #floor division

        #Dividing the array elements into 2 halves
        L = array[:mid]
        R = array[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        #Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        #Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

arr = [12,3,11,13,5,6,7]
print("Original List:\t", arr)
mergeSort(arr)
print("Sorted List: \t", arr) 
