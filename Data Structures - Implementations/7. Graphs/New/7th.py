# Prim's and Kruskal's

"""
Prim's algorithm
Prim's algorithm is a minimum spanning tree algorithm that takes a graph as input and
finds the subset of the edges of that graph which form a tree that includes every vertex
has the minimum sum of weights among all the trees that can be formed from the graph

How Prim's algorithm works

It falls under a class of algorithms called greedy algorithms that find the local optimum in the hopes of finding a global optimum.
We start from one vertex and keep adding edges with the lowest weight until we reach our goal.

The steps for implementing Prim's algorithm are as follows:

    1. Initialize the minimum spanning tree with a vertex chosen at random.
    2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
    3. Keep repeating step 2 until we get a minimum spanning tree
"""

import heaqp

# Given a list of edges of a connected unidirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the MST
def minimumSpanningTree(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []

    for n1, n2, wieght in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])

    # Initialize the heap by choosing a single node
    # (in this case 1) and pushing all its neighbors

    minHeap = []
    for neighbor, wieght in adj[1]:
        heapq.heappush(minHeap, [wieght, 1, neighbor])

    mst = []
    visit = set()
    visit.add(1)

    while len(visit) < n:
        weight, n1, n2 = heapq.heappop(minHeap)
        if n2 in visit:
            continue

        mst.append([n1, n2])
        visit.add(n2)

        for neighbor, weight in adj[n2]:
            if neighbor not in visit:
                heapq.heappush(minHeap, [wieght, n2, neighbor])

    return mst


# The time complexity of Prim's algorithm is O(E log V).

# Prim's Algorithm Application
#
#     Laying cables of electrical wiring
#     In network designed
#     To make protocols in network cycles
#


"""
Kruskal's algorithm
It is a minimum spanning tree algorithm that takes a graph as input and finds the subset
of the edges of that graph which form a tree that includes every vertex
has the minimum sum of weights among all the trees that can be formed from the graph


It falls under a class of algorithms called greedy algorithms that find the local optimum in the hopes of finding a global optimum.
We start from the edges with the lowest weight and keep adding edges until we reach our goal.
The steps for implementing Kruskal's algorithm are as follows:

    1. Sort all the edges from low weight to high
    2. Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
    3. Keep adding edges until we reach all vertices.


PsudoCode
Any minimum spanning tree algorithm revolves around checking if adding an edge creates a loop or not.
The most common way to find this out is an algorithm called Union Find. 
The Union-Find algorithm divides the vertices into clusters and allows us to check
if two vertices belong to the same cluster or not and hence decide whether adding an edge creates a cycle.

"""
import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    # Find parent of n, with path compression
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    # Union by height/rank
    # Return false if already connected, true otherwise
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        return True


# Given a lit of edges of a connected undirected graph,
# with nodes numbered from 1 to n
# return a list edges making up the minimum spanning tree


def minimumSpanningTree(edges, n):
    minHeap = []
    for n1, n2, weight in edges:
        heapq.heappush(minHeap, [weight, n1, n2])

    unionFind = UnionFind(n)
    mst = []

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)
        if not unionFind.union(n1, n2):
            continue
        mst.append([n1, n2])
    return mst


"""


The time complexity Of Kruskal's Algorithm is: O(E log E).
Kruskal's Algorithm Applications

    1. In order to layout electrical wiring
    2. In computer network (LAN connection)


"""


"""

Kruskal's vs Prim's Algorithm

Prim's algorithm is another popular minimum spanning tree algorithm that uses a different logic to find the MST of a graph.
Instead of starting from an edge, Prim's algorithm starts from a vertex and keeps adding lowest-weight edges which aren't in the tree,
until all vertices have been covered.
Kruskal's Algorithm Complexity
"""
