def find_grants_cap(grantsArray, newBudget):
  
    n = len(grantsArray)

    # Sort the array in a descending order
    grantsArray.sort(reverse = True)
    
    # append a zero with end of array to cover the case where 0 <= cap <= grantsArray[i]
    grantsArray.append(0)

    # Calc total amount we need to cutback to meet the reduced budget
    surplus = sum(grantsArray) - newBudget

    # If there is nothing to cut, simply return the highest grant as the cap.
    if surplus <= 0:
        return grantsArray[0]

    # Start subtracting from surplus the differences("deltas") between consecutive grants until surplus is less
    # or equal to zero. Basicallym we are testing out , in order, each of the grants as potential lower bound for the cap.
    # Once we find out the first value, that brings us below zero we break
    for i in range(0, n-1):
        surplus -= (i + 1) * (grantsArray[i] - grantsArray[i+1])
        if surplus <= 0:
            break
    wayfair 

    # Since, grantsArray[i+1] is a lower bound to our cap, i.e grantsArray[i+ 1] <= cap,
    # We need to add to grantsArray[i+1] the difference: (-total / float(i+1)), so the returned value equals exactly to  cap
    return grantsArray[i+1] + (-surplus/float(i + 1))
    

# Driver Code
grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190

print(find_grants_cap(grantsArray, newBudget))
