# Topological Sort
# Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
# Output: Following are the two valid topological sorts for the given graph:
# 1) 3, 2, 0, 1
# 2) 3, 2, 1, 0

from collections import deque


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= n:
        return sorted_order

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # Count of incoming edges
    graph = {i: [] for i in range(vertices)}  # Adjacency List Graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # Put the child into it's parent's list
        in_degree[child] += 1

    # c. Find all the sources, i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from all of it's
    # children's in-degrees, if a child's in-degree becomes zero, add it to the source's queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        for child in graph[
            vertex
        ]:  # Get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # Topological Sort is not possible as graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order


def main():
    print(
        "Topological sort: "
        + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    )
    print(
        "Topological sort: "
        + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    )
    print(
        "Topological sort: "
        + str(
            topological_sort(
                7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
            )
        )
    )


main()
