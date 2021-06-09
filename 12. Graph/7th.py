# Minimum steps to reach target by a Knight
# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

# Python3 code to find minimum steps to reach to specific cell in minimum moves by Knight

class cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

# Check whether given position is inside the board


def isInside(x, y, N):
    if(x >= 1 and x <= N and y >= 1 and y <= N):
        return True
    return False

# Method returns minimum steps to reach target position


def minStepToReachTarget(knightPos, targetPos, N):
    # All possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []

    # Push starting position of knight with 0 distance
    queue.append(cell(knightPos[0], knightPos[1], 0))

    # Make all cell unvisited
    visited = [[False for i in range(N + 1)] for j in range(N+1)]

    # loop until we have one element in the queue
    while(len(queue) > 0):
        t = queue[0]
        queue.pop(0)

        # If current cell is equal to target cell, return it's distance
        if(t.x == targetPos[0] and t.y == targetPos[1]):
            return t.dist

        # Iterate for all reachable states
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]

            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist +1))

# Driver Code
if __name__ == "__main__":
    N = 30
    knightPos = [1, 1]
    targetPos = [30, 30]
    print(minStepToReachTarget(knightPos, targetPos, N))
