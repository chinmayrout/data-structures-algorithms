#  Multi-source BFS - Walls and Gates problem LC - 286


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Multi-Source-BFS
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # left, up, right, down

        if not rooms:
            returns

        ROWS, COLS = len(rooms), len(rooms[0])

        # 1. Find all gates
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        # 2. Find shortest distance to gate: BFS
        while queue:
            r, c = queue.popleft()

            dist = rooms[r][c] + 1

            for dr, dc in directions:
                row, col = r + dr, c + dc

                if row in [-1, ROWS] or col in [-1, COLS]:
                    continue

                if (
                    dist < rooms[row][col]
                ):  # No check if cell is a wall as dist will always > -1
                    rooms[row][col] = dist
                    queue.append((row, col))


"""
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Input: rooms = [[-1]]
Output: [[-1]]



"""
