#find duplicate in an array of N+1 Integers


#==========================================
#O(n^2) way
def dup(arr):
    size = len(arr)
    repeated = []
    for i in range(size):
        for j in range(i + 1, size):
            if arr[i] == arr[j] and arr[i] not in repeated: #only add duplicated values once
                repeated.append(arr[i])
    return repeated

#Driver Code
arry = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(dup(arry))






#==========================================
#dictionary approach
#Use Dictionary to store number as key and it’s frequency as value. Dictionary can be used as range of integers is not known.
def printDuplicates(arr):
    dict = {}

    for i in arr:
        try:
            dict[i] += 1    #try to  add the value of (key=ith) 
			# if the key exists in dict then increment its value(try);otherwise assign one value(except)
        except:
            dict[i] = 1	#now adding key-value
	#after above for loop new dictionary is created with
	#{10: 1, 20: 3, 30: 2, 40: 1, 50: 1, -20: 3, 60: 2}

    for i in dict:
        #if frequency is more than 1, print the element
        if dict[i] > 1:
            print(i,end = " ")
			

    print("\n")

#Driver Code
arry1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
printDuplicates(arry1)

#==========================================
#XOR solution
def findDupXOR(nums):
    n = len(nums)
    x = 0
    for i in range(1, n-1):
        x = x ^ i

    y = 0
    for i in range(n):
        y = y ^ nums[i]

    return x ^ y

#Driver Code
arry2 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(findDupXOR(arry2))