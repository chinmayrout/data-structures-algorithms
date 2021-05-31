def kedane(arr):
    max_so_far = arr[0]
    max_ending_here = 0

    for i in range(0, len(arr)):
        max_ending_here = max_ending_here + arr[i]

        if max_ending_here < 0:
            max_ending_here = 0

        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        

    return max_so_far

arr= [-1,-1,-2,3,-2,-3,2,2,3,4]
print(kedane(arr))
