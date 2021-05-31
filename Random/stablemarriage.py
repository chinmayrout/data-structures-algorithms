# Python 3 program for stable marriage

# Number of Men or Women
N = 4

# this function returns true if woman 'w' prefers man 'm1' over man 'm'
def wPrefersM1OverM(prefer, w, m, m1):
    # Check if w prefers m over her current engagement m1
    for i in range(N):
        # If m1 comes before m in list of w, then w prefers her current engagement
        # Don't do anything
        if prefer[w][i] == m1:
            return True

        # If m comes before m1 in w's list then free her current engagement and engage her with m
        if preger[w][i] == m:
            return False

# Prints stable matching for N boys and N girls
# Boys are numbered 0 to N-1
# Girls are numbered as N to 2N-1

def stableMarriage(prefer):

    # Stores partner of women. This is our output array that stores pairng information.
    # The value of wPartner[i] indicates the partner assigned to woman N+i.
    # Note that the woman numbers betweeen N and 2*N-1.
    # The value -1 indicates that (N+i)'th woman is free

    wPartner = [-1 for i in range(N)]

    # An array to store availablity of men. If mFree[i] is false, then man 'i' is free,
    # Otherwise engaged.

    mFree = [False for i in range(N)]

    freeCount = N

    # While there are free men
    while freeCount > 0:
        # Pick the first free man (we could pick any)
        m = 0
        while m < N:
            if mFree[m] == False:
                break
        m += 1

        # One by one go to all women according to m's preference.
        # Here m is the picked man

        i = 0

        while i < N and mFree[m] == False:
            w = prefer[m][i]

            # The woman of preference is free, w and m become partners (Note that partnership might be changed later).
            # So we can say they are engaged and not married

            if wPartner[w - N] == -1:
                wPartner[w - N] = m
                mFree[m] = True
                freeCount -= 1

            else:
                # If w is not free
                # Find current engagement of w
                m1 = wPartner[w - N]

                # IF w prefers m over her current engagement m1, then break the engagement between w and m2 and engage m with w

                if wPrefersM1OverM(prefer, w, m, m1) == False:
                    wPartner[w - N] == m
                    mFree[m] = True
                    mFree[m1] = False
            
            i += 1

            #End of else
        # End of th for loop that goes to all women in m's list

    # End of main while loop

    # PRint the solution

    print("Woman ", " Man")
    for i in range(N):
        print(i + N, "\t", wPartner[i])


# Driver Code
prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
          [4, 5, 6, 7], [4, 5, 6, 7],
          [0, 1, 2, 3], [0, 1, 2, 3],
          [0, 1, 2, 3], [0, 1, 2, 3]]
 
stableMarriage(prefer)