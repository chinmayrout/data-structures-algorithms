# Detect Cycle in UnDirected Graph using BFS/DFS Algo 
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/


# Python Program to detect cycle in an unidirected graph
from collections import defaultdict

# This class represents a unidirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # Number of vertices
        self.V = vertices       #Number of vertices
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        # Add v to u_s list
        self.graph[u].append(v)
        # Add u to v_s list
        self.graph[v].append(u)


    # A recurise function that uses visited[] and parent to detect cycle in subgraph reachable from vertex v
    def isCyclicUtil(self, v, visited, parent):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
                # If an adjacent vertex is visited and not parent of current vertex, then there is a cycle
                elif parent != i:
                    return True
            
            return False

    
    # Returns true if the graph contains cycle, else false
    def isCyclic(self):
        # Mark alll ther vertices as not visited
        visited = [False] * (self.V)

        # Call the recursive helper function to detect cycle in the different DFS tree
        for i in range(self.V):
            # Don't recur fr u if it is already visited
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, -1) == True:
                    return True
        return False



#Driver Code
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)


if g.isCyclic():
    print("Graph contains cycle")

else:
    print("Graph doesn't contain a cycle")

g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)

if g1. isCyclic():
    print("Graph contains cycle")

else:
    print("Graph doesn't contain a cycle")



























'''
Algorithm: 

1. Create the graph using the given number of edges and vertices.
2. Create a recursive function that that current index or vertex, visited and recursion stack.
3. Mark the current node as visited and also mark the index in recursion stack.
4. Find all the vertices which are not visited and are adjacent to the current node. Recursively call the function for those vertices, If the recursive function returns true return true.
5. If the adjacent vertices are already marked in the recursion stack then return true.
6. Create a wrapper class, that calls the recursive function for all the vertices and if any function returns true, return true.
7. Else if for all vertices the function returns false return false.
'''