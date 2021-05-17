#Python Code of Bubble-Sort
#Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them if they are not in the intended order.


def bubbleSort(array):

    #loop to access each array element
    for i in range(len(array)):

        #loop to compare elements
        for j in range(0, len(array) - i - 1):

            #compare two adjacent elements
            #change > to < to sort in descending order
            if array[j] > array[j + 1]:
                #swapping elements if elements are not in order

                array[j] , array[j+1] = array[j+1], array[j]


data = [-2, 43, 0, 12, -9]
print("Original Data",data)
bubbleSort(data)

print('Sorted Array in Ascending order is : ')
print(data)

#=============================================================================================
#Optimized Bubble Sort Algorithm

def optimizedBubbleSort(array):

    #Loop through each element in array
    for i in range(len(array)):

        #keep track of swapping
        swapped = False

        #loop to compare array elements
        for j in range(0, len(array) - i - 1):

            #compare two adjacent elements
            #change > to < to sort in descending order

            if array[j] > array[j+1]:
                #swapping occurs if elements are not in intended order
                array[j], array[j+1] = array[j+1], array[j]

                swapped = True
            

        #no swapping means the array is already sorted, so no need for further comparison
        if not swapped:
            break

data1 = [-2, 43, 0, 12, -9]
print("Original", data1)
optimizedBubbleSort(data1)
print(data1)