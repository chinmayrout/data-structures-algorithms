def printDuplicates(arr):
	dict = {}

	for i in arr:
		if i in dict.keys():
			dict[i] += 1

		else:
			dict[i] = 1

	for i in dict:
		if dict[i] > 1:
			print(i, end = " ")

	print("\n")

#Driver Code
arr = [1,1,3,2,1,2]
printDuplicates(arr)