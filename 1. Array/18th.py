# find all pairs on integer array whose sum is equal to given number


'''
1. Create a map to store frequency of each number in the array. (Single traversal is required)
2. In the next traversal, for every element check if it can be combined with any other element (other than itself!) to give the desired sum. Increment the counter accordingly.
3. After completion of second traversal, we’d have twice the required value stored in counter because every pair is counted two times. Hence divide count by 2 and return.

'''

def getPairsCount(arr, n, sum):
    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1

    twice_count = 0

    # Iterate through each elmeent and increment the count (Notice that every pair is counted twice)

    for i in range(0, n):
        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the condition, then we need to ensure that the count is decreased by one such that
        # (arr[i], arr[i]) pair is not considered

        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # Return the half of twice_count
    return int(twice_count/2)



# Driver Function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6

print("Count of pairs is: ",getPairsCount(arr, n, sum))