# Search an element in a matriix

def findRow(arr, noRows, noCols, k):
    l = 0
    r = noRows -1
    mid = 0
    while(l <= r):
        mid = int((l + r) / 2)

        # we'll check the left and right most elements of the row here itself for efficiency
        if(k == arr[mid][0]):     #Checking leftmost element
            print("Found at(", mid , ",","0)", sep = "")
            return

        if(k == arr[mid][noCols - 1]):     # Checking rightmost element
            t = noCols - 1