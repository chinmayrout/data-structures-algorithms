# Selection Sort in Python
# Selection sort is a sorting algorithm that selects the smallest element from an unsorted list 
# in each iteration and places that element at the beginning of the unsorted list.

def selectionSort(array):

    for step in range(len(array)):
        min_idx = step  #min_idx is the index of minimum element

        for i in range(step+1, len(array)):

            #to sort in descending order, change > to <
            #select the minimum element in each loop

            if array[i] < array[min_idx]:
                min_idx = i

        #put min at the correct position
        array[step], array[min_idx] = array[min_idx], array[step]

data = [-1, -3, 1, 4, 0]
print("Original Data: \t", data)
print("\n")
selectionSort(data)
print("Sorted Data: \t", data)

'''
TIME AND SPACE COMPLEXITY:
Time Complexity	 
Best	            O(n2)
Worst	            O(n2)
Average	            O(n2)
Space Complexity	O(1)
Stability	        No

USES:
- a small list is to be sorted
- cost of swapping does not matter
- checking of all the elements is compulsory
- cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)





'''
