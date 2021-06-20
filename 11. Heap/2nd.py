# Sort an Array using heap. (HeapSort)
# https://www.geeksforgeeks.org/heap-sort/
'''
Algo:
1. Build a max heap from the input data. 
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree. 
3. Repeat step 2 while the size of the heap is greater than 1.
'''

# Heapify subtree rooted at index i and n is the size of heap

def heapify(arr, n, i):
    largest = i     # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child of root exists and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Check if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]         # Swap

        # Heapify the root
        heapify(arr, n, largest)



# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxHeap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
    
# Driver Code
arr = [12, 10, 13, 5, 8, 9]
heapSort(arr)
n = len(arr)
print("Sorted Array is:", arr)