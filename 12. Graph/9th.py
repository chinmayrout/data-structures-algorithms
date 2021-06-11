# Clone a undirected graph
# https://leetcode.com/problems/clone-graph/solution/

from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add edge to the graph
    def addEdge(self, u, v):
        # Add v to u_s list
        self.graph[u].append(v)
        # Add u to v_s list
        self.graph[v].append(u)
