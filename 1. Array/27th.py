# Find whether an array is a subset of another array

def arrySub(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    s = set()
    for i in range(n):
        s.add(arr1[i])

    p = len(s)

    for i in range(m):
        s.add(arr2[i])

    if(len(s) == p):
        print("arr2 is subset of arr1")
    else:
        print("Not a subset")


# Driver Code

arr1 = [11,1, 13,21, 3, 7]
arr2 = [11, 3, 7,1]
arr3 = [112, 3, 7,1]

arrySub(arr1, arr2)
arrySub(arr1, arr3)