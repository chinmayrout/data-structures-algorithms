#Iterative Merge Sort using Python
# Bottom Up Approach
#Pending**

def mergeSort(a):
    current_size = 1

    #Outer loop for traversing each sub-array of current_size
    while current_size < len(a) - 1:

        left = 0
        #Inner loop for merge call in a sub-array
        #Each complete iteration sorts the iterating sub array
        while left < len(a) - 1:
            #mid index = left index of sub-array + current sub-array size - 1

            mid = min((left + current_size - 1),(len(a) - 1))

            #(False result, True result)