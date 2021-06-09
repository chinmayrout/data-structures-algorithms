# Rat in a Maze Problem/Rat in a Maze Problem when movement in all possible directions is allowed
# https://www.geeksforgeeks.org/rat-in-a-maze-problem-when-movement-in-all-possible-directions-is-allowed/
from typing import List

MAX = 5

# Function returns true if the move taken is valid else it will return false.
def isSafe(row: int, col: int, m: List[List[int]], n: int, visited: List[List[bool]]) -> bool:
    if (row == -1 or row == n or col == -1 or col == n or visited[row][col] or m[row][col] == 0):
        return False
    return True

# Function to print all the possible paths from (0, 0) to (n-1, n-1)
def printPathUtil(row: int, col:int, m: List[List[int]], n: int, path: str, possiblePaths: List[str], visited: List[List[bool]]) -> None:
    # This will check the initial point (i.e. (0, 0)) to start the paths
    if row == -1 or row == n or col == -1 or col == n or visited[row][col] or m[row][col] == 0:
        return

    # If reach the last cell(n-1, n-1) then store the path and return
    if row == n - 1 and col == n - 1:
        possiblePaths.append(path)
        return

    # Mark the cell as visited
    visited[row][col] = True

    # Try for all the 4 directions(down, left, right, up) in the given order to get the paths in lexicographical order

    # Check if downward move is valid
    if (isSafe(row +1, col, m, n, visited)):
        path += 'D'
        printPathUtil(row + 1, col, m, n, path, possiblePaths, visited)
        path = path[:-1]


    # Check if the left move is valid
    if(isSafe(row, col - 1, m, n, visited)):
        path += 'L'
        printPathUtil(row, col - 1, m, n, path, possiblePaths, visited)
        path = path[:-1]

    # Check if right move is valid
    if(isSafe(row, col + 1, m, n, visited)):
        path += 'R'
        printPathUtil(row, col + 1, m, n, path, possiblePaths, visited)
        path = path[:-1]

    # Check if down move is valid
    if(isSafe(row - 1, col, m, n, visited)):
        path += 'U'
        printPathUtil(row - 1, col, m, n, path, possiblePaths, visited)
        path = path[:-1]

    # Mark the cell as unvisited for other possible paths
    visited[row][col] = False


#Function to store and print all the valid paths
def printPath(m: List[List[int]], n: int) -> None:
    # List to store all the possible paths
    possiblePaths = []
    path = ""
    visited = [[False for _ in range(MAX)] for _ in range(n)]

    # Call the utility function to find the valid paths
    printPathUtil(0, 0, m, n, path, possiblePaths, visited)

    # Print all possible paths
    for i in range(len(possiblePaths)):
        print(possiblePaths[i], end = " ")


# Driver Code
if __name__ == "__main__":
    m = [   [ 1, 0, 0, 0, 0],
            [ 1, 1, 1, 1, 1],
            [ 1, 1, 1, 0, 1],
            [ 0, 0, 0, 0, 1],
            [ 0, 0, 0, 0, 1]    ]
    n = len(m)
    printPath(m, n)



'''
1. Start from the initial index (i.e. (0,0)) and look for the valid moves through the adjacent cells in the order Down->Left->Right->Up (so as to get the sorted paths) in the grid.
2. If the move is possible, then move to that cell while storing the character corresponding to the move(D,L,R,U) and again start looking for the valid move until the last index (i.e. (n-1,n-1)) is reached.
3. Also, keep on marking the cells as visited and when we traversed all the paths possible from that cell, then unmark that cell for other different paths and remove the character from the path formed.
4. As the last index of the grid(bottom right) is reached, then store the traversed path.
'''