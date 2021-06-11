# Maximum size rectangle
# https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/

# Finds the maximum area under the histogram represented by histogram
def maxHist(row):
    # Create an empty stack. The stack holds indexes of hist array.
    # The bars stored in stack are always in increasing order of their heights
    result = []

    # Top of stack
    top_val = 0

    # Initialize max area in current
    max_area = 0
    
    # Row (or histogram)
    area = 0        # Initialize area with current top

    # Run through all bars of given histogram (or row)
    i = 0
    while i < len(row):
        # If this bar is higher than the bar on the top stack, push it to the stack
        if (len(result) == 0) or (row[result[-1]] <= row[i]):
            result.append(i)
            i+=1
        else:
            # If this bar is lower than top of stack, then calculate area of rectangle with
            # stack top as the smallest (or minimum height) bar. 'i' is 'right index' for
            # the top and element before top in stack is 'left index'
            top_val = row[result.pop()]
            area = top_val * i

            if (len(result)):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)

    # Now pop the remaining bars from stack and calculate area with every popped bar as the smallest bar
    while(len(result)):
        top_val = row[result.pop()]
        area = top_val * i
        if (len(result)):
            area = top_val * (i - result[-1] - 1)

        max_area = max(area, max_area)

    return max_area



# Returns area of the largest rectange with all 1s in A
def maxRectange(A):
    # Calculate area for first row and initialize it as result
    result = maxHist(A[0])

    # Iterate over row to find maximym rectangular area considering 
    # wach row as histogram
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            # If A[i][j] is 1 then add A[i - 1][j]
            if (A[i][j]):
                A[i][j] += A[i - 1][j]

        # Update result if area with current row(as last row) of rectange is more
        result = max(result, maxHist(A[i]))

    return result

# Driver Code
A = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

print("Area of maximum rectange is: ", maxRectange(A))