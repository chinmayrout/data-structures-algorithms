# Matrix Representation + BFS and DFS of Matrix


# Matrix (2D Grid)

grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

# DFS - Count paths(backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
        return 0

    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count += 0

    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))

    return count


# BFS - Shortest path from top left to  bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    queue = deque()  # For the level of BFS
    queue.append((0, 0))

    visit.add((0, 0))

    length = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()  # popping out the co-ordinates
            if r == ROWS - 1 and c == COLS - 1:  # reached the destination
                return length

        neighbors = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]  # All 4 neighbors/directions// right, left, bottom, top

        for dr, dc in neighbors:  # dr is difference in row, dc is difference in column
            if (
                min(r + dr, c + dc) < 0
                or r + dr == ROWS
                or c + dc == COLS
                or (r + dr, c + dc) in visit
                or grid[r + dr][c + dc] == 1
            ):
                continue
            # Now for valid position
            queue.append((r + dr, c + dr))  # Add to queue
            visit.add((r + dr, c + dc))  # Add to visit set
    length += 1  # Increase the length, to show nodes can be visited with layer + 1


# BFS is more effiencent, T - O(m.n)
#
