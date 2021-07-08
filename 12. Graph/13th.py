# A directed acyclic graph (DAG) is a directed graph with no directed cycles.
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.
# Topological Sorting for a graph is not possible if the graph is not a DAG.
# In DFS, we print a vertex and then recursively call DFS for it's adjacent vertices.
# In TS, we need to print a vertex before it's adjacent vertices.

'''
# Algo
In topological sorting, we use a temporary stack. We don't print the vertex immediately, we first recursively call topological
sorting for all it's adjacent vertices, then push it to the stack.
Finally, print the contents of the stack.
'''
# Python Program to print topological sorting of a DAG
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)      # dictionary containing the adjacency list
        self.V = vertices

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        
        # Push current vertex to stack which stores result
        stack.append(v)

    # This function is to perform the Topological Sort. It uses the recursive topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological Sort starting from
        # all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        print(stack[::-1])      # Return list in reverse order

# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")

# Function Call
g.topologicalSort()

'''
Time Complexity: O(V+E). 
The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS which is.
Auxiliary space: O(V). 
The extra space is needed for the stack.
'''