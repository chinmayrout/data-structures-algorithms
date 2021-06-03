# Given an array of size n and a number k, fin all elements that appear more than " n/k " times.

def morethanNbyK(arr, n, k):
    x = n // k

    # Making a dictionary
    freq = {}

    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    # Traversing the map
    for i in freq:
        # Checking if value of a key-value pair is greater than x (where x = n/k)
        if (freq[i] > x):
            # Print the key of whose value is greater than x
            print(i)


# Driver Code
arr = [ 1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1 ]
n = len(arr)
k = 4
  
morethanNbyK(arr, n, k)