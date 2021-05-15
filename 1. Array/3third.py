#K’th Smallest/Largest Element in Unsorted Array

def sol1(array, k):

    array.sort()

    return array[k - 1]

arr = [12, 3, 6, 11, 9, 1, 0]
k = int(input("Enter k value"))     
print("Kth smallest element is", sol1(arr,k))


#QuickSelect
#Standard Partition process of QuickSort. It considers the last element as pivot and moves all smalller element to left of it and 
# greater elements to right
def partition(array, left, right):

    x = array[right]
    i = left
    for j in range(left, right):

        if array[j] <= x:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[r] = array[r], array[i]
    return i

#finds the kth position of the sorted array in a given unsorted array i.e. this funciton can be used to find both kth largest and 
#kth smalllest element in the array. 
#ASSUMPTION: All elements in arr[] are distinct

def kthSmallest(arr, left, right, k):

    #if k is smaller than number of elements in array
    if(k > 0 and k <= right - left + 1):

        #Partition the array around last element andget position of pivot element in sorted array
        index =  partition(arr, left, right)

        #if the position is same as k
        if(index - left == k - 1):
            return arr[index]
        #if psition is more, recur from left subarray
        if(index - left > k -1):
            return kthSmallest(arr, left, index - 1, k)
        
        #else recur for right subarray
