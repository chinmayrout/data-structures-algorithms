# Python code for adding one to the number represented by digits

def incrementNumberArr(arr):
    n = len(arr)

    # Add 1 to the last digit and find carry
    arr[n-1] += 1
    carry = arr[n-1]/10
    arr[n-1] = arr[n-1] % 10

    # Traverse from second last digit
    for i in range(n-2, -1, -1):
        if carry == 1:
            arr[i] += 1
            carry = arr[i] / 10
            arr[i] = arr[i] % 10

    # If carry is 1, we need to add 1 at the beginnning of array
    if carry == 1:
        a.insert(0, 1)

# Driver Code
arr = [1, 8, 8, 9]
incrementNumberArr(arr)

print(arr)