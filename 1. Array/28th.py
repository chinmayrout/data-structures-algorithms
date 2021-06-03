'''
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. 
If there is such a triplet present in array, then print the triplet and return true. Else return false.
'''

# Find the triplet that sum to a given value

def find3Numbers(A, summ):
    n = len(A)
    for i in range(0, n - 1):
        # Find pair in subarray A[i+1...n-1] with sum equal to sum - A[i]
        s = set()
        curr_sum = summ - A[i]
        for j in range(i+1, n):
            if curr_sum - A[j] in s:
                print('Triplet is', A[i], ", ", A[j], ", ", curr_sum - A[j])

                return True
            s.add(A[j])
    print("Not present")
    return False


# Driver Code
A = [1, 4, 45, 6, 10, 8] 
summ = 22
summ1 = 100
find3Numbers(A, summ)
find3Numbers(A, summ1)
