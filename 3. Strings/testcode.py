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