# Merge Two Sorted Arrays with O(1) extra space -   pending

# https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/

def merg(arr1, arr2):

    m = len(arr1)+1
    n = len(arr2)+1

    # Set p1 and p2 to point to the end of their respective arrays.
    p1 = m - 1
    p2 = n - 1

    for p in range(n + m-1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and arr1[p1] > arr2[p2]:
            arr1[p] = arr1[p1]
            p1 -= 1
        else:
            arr1[p] = arr2[p2]
            p2 -= 1


arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
merg(arr1,arr2)

print("After Merging", *arr1, *arr2)
