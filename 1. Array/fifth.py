#Move all the negative elements to one side of the array 

def sol1(arr):      #using the quicksort
    j = 0
    for i in range(0, len(arr)):
        if(arr[i] < 0):
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    print(arr)

#Driver Code
arr=[-12, 11, -13, -5, 6, -7, 5, -3, 11]
sol1(arr)