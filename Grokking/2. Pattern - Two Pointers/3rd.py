# Squaring a Sorted Array (easy): LC 977 ✅
def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]

    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1

        highestSquareIdx -= 1
    return squares

# Driver Code
arr = [-4,-1,0,3,10]

print(make_squares(arr))