# Implement DFS Algo 
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

# Python program to print DFS traveral for complete graph
from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    #Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the cutrrent node as visited and print it
        visited.add(v)
        print(v)

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # This function does DFS traversal. It uses recursive DFSUtil()
    def DFS(self):
        # Create a set to store all visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal starting from all vertices one by one
        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex, visited)


# Driver Code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal")
g.DFS()