# Python programn for Insertion Sort Algorithm
# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]

        j = step - 1

        #Compare key with each element on the left of it until an element smaller than it is found
        #For descending order, change key<array[i] to key>array[j]

        while j >=0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element is smaller than it
        array[j + 1] = key

data = [9, 1, 5, 4, 3]
insertion_sort(data)
print('Sorted Array in ascending order: ')
print(data)


'''

Time Complexity	 
Best	O(n)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	Yes

Uses:
- the array is has a small number of elements
- there are only a few elements left to be sorted

https://en.wikipedia.org/w/index.php?title=Insertion_sort&oldid=1022522065
'''
