# Given an array of size n and a number k, fin all elements that appear more than " n/k " times.

def morethanNbyK(arr, k):
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
