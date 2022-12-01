# Dijkstra's Algo
# Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph.
#
# It differs from the minimum spanning tree because the shortest distance between two vertices
# might not include all the vertices of the graph.

# How Dijkstra's Algorithm works
# Dijkstra's Algorithm works on the basis that any subpath B -> D of the shortest path A -> D between
# vertices A and D is also the shortest path between vertices B and D.

# Almost like BFS

# shortest subpath property is used by dijkstra's algorithm
# Each subpath is the shortest path
# Djikstra used this property in the opposite direction i.e we overestimate the distance of each vertex from the starting vertex.
# Then we visit each node and its neighbors to find the shortest subpath to those neighbors.

# The algorithm uses a greedy approach in the sense that we find the next best solution
# hoping that the end result is the best solution for the whole problem.

# We need to maintain the path distance of every vertex. We can store that in an array of size v, where v is the number of vertices.
# We also want to be able to get the shortest path, not only know the length of the shortest path. For this, we map each vertex to the vertex that last updated its path length.
# Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.
# A minimum priority queue can be used to efficiently receive the vertex with least path distance.

import heapq

# Given a connected graph represented by a list of edges, where egde[0] = src, edge[1] = dst and edge[2] = weight,
# Find the shortest path from src to every other node in the graph.
# There are n nodes in the graph


def shortestPath(edges, n, src):
    adj = {}

    for i in range(1, n + 1):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append([d, w])

    shortest = {}

    minHeap = [[0, src]]

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, [w1 + w2, n2])

    return shortest


# Dijkstra's Algorithm Complexity
# Time Complexity: O(E Log V), O(E * logE) is also correct.

# where, E is the number of edges and V is the number of vertices.
# We can add V^2 nodes at max to to min-heap
# Min heap uses LogV^2 ~ LogV
# Min heap can be filled E times
# ElogV

# Space Complexity: O(V)

# Dijkstra's Algorithm Applications
# To find the shortest path
# In social networking applications
# In a telephone network
# To find the locations in the map
