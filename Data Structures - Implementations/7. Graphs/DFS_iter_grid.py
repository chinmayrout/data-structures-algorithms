# DFS(iterative) on Matrix

from collections import deque


def dfs(matrix):
    # Check for an empty graph.
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    result = []

    def traverse(i, j):
        if (i, j) in visited:
            return 0

        stack = deque([(i, j)])
        while stack:
            curr_i, curr_j = stack.pop()
            if (curr_i, curr_j) not in visited:
                visited.add((curr_i, curr_j))
                result.append(matrix[curr_i][curr_j])

                for direction in directions:
                    next_i = curr_i + direction[0]
                    next_j = curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        # Add in your question specific checks
                        stack.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
    return result


grid = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
print(dfs(grid))


'''
DFS and BFS on a grid are similar. Just do a pop() on the stack instead of popleft() on the queue.
'''


for j in range(len(avg)):
if avg[j] < 25:
if (instance > 1):
instance = math.ceil(instance / 2)
j = j+10
if j > len(avg):
break
if avg[j] > 60:
if ((instances*2) < 217):
instance = instance * 2
j = j+10
if j > len(avg):
break
return (instance)
