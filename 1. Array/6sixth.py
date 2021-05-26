#Find the Union and Intersection of the two sorted arrays.
#using sets

def printUnion(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    hs = set()

    #Insert the elements of arr1[] into set hs
    for i in range(0, n1):
        hs.add(arr1[i])

    #Insert the elements of arr2to set hs
    for i in range(0, n2):
        hs.add(arr2[i])

    print("Union:")

    for i in hs:
        print(i, end= " ")      #https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
    print("\n")
    #Prints union of arr1 and arr2

def printIntersection(arr1, arr2):
    hs = set()
    n1 = len(arr1)
    n2 = len(arr2)

    for i in range(0, n1):
        hs.add(arr1[i])
    print("Intersection:")
    for i in range(0, n2):
        # If element is present in set then print it out

        if arr2[i] in hs:
            print(arr2[i], end =" ")
    print("\n")
#Driver Program
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]

#Function call
printUnion(arr1, arr2)
printIntersection(arr1, arr2)
    