#Minimum no. of Jumps to reach end of an array
# https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/

#check intendation correctly
#Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr):
    n = len(arr)

    if n <= 1:  #The number of jumps needed to reach the starting index is 0
        return 0
   
    if arr[0] == 0:  #Return -1 if not possible to loop
        return -1

    #initialization
    maxReach = arr[0]   #Stores all time the maximal reachable index in the array
    step = arr[0]   #stores the amount of steps we can still take
    jump = 1    #stores the amount of jumps necessary to reach that maximal reachable position

    #Start traversing the array
    for i in range(1, n):
        if (i == n-1):      #Check if we have reached the end of the array
            return jump

        maxReach = max(maxReach, i + arr[i])    #Updating maxReach
        step -= 1       #we use a step to get to the current index

        if step == 0:   #if no further step left
            jump += 1

            if i >= maxReach:   #Check if the current index or lesser index is the maximum reach point from previous index
                return -1

            step = maxReach - i #re-initialize the steps to amount of steps to reach maxReach from position i

    return -1

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9 ]
print(minJumps(arr))


#Algo:3
# 1. Check if the first element of the array is equal to 0 if true then return -1.
# 2. Set the maxValue and stepTaken to the first element of the given array.
# 3. Set jumpTaken to 1.
# 4. Traverse the array from i=1 to i<n(length of the array).
#   1. If the last element of the array reached, return jumpTaken.
#   2. Find out the maximum value between the maxValue and arr[i] + i and store it to maxValue.
#   3. Decrease the value of stepTaken by 1.
#   4. If stepTaken is equal to 0.
#     1. Increase jumpTaken by 1.
#     2. Check if i is greater than maxValue
#       Return -1.
#   5. Set stepTaken to maxValue-i.
# 5. Return -1.