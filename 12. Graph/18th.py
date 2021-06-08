# Kruskal’s Minimum Spanning Tree Algorithm 
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/


# Python program for Kruskal's algorithm to find MST of a given connected unidirected and weighted graph
from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices       # No. of vertices
        self.graph = []         # default deictionary
        # To store graph

    
    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    
    # A utility function to find set of two sets of x and y (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree(Union by rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        
        # If ranks are same, then make one as root and increment it's rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    # The main function  is to construct MST using Kruskal's Algortihm
    def KruskalMST(self):
                