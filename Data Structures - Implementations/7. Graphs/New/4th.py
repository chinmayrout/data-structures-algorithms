# Union-Find Data Structure (A.K.A. Disjoint Set Data Structure)
# A tree-DS but usally in a Graph
# We have disjoint sets eg -> two graphs
# Can be used to count the number of connected components
# Can also be used for cycle detection

# DFS can solve this problem, but UF is easier/better to implement
# Union find is basically a forest of trees

# Start with individual node and make each node it's parent
# Take a node and set it as parent and another node which it has an edge with (arbitrary)
# Go to root of each tree and union with another tree

# Union by rank(height) -> Take smaller height tree and add to larger height tree
# If root of two nodes are the same, they are part of same connected component,
# We can't union in this case as they are part of same set, return False for union
# in this case, graph has cycle

# UF doesn't accurately represent the graph, it's about finding cycles and count number
# connected components


class UnionFind:
    def __init__(self, n):  # Constructor takes size of the set
        self.parent = {}  # For taking parents of each node
        self.rank = {}  # Track of rank(height) of each node

        for i in range(1, n + 1):  # Start from 1
            self.parent[i] = i  # Initialize parent to itself
            self.rank[i] = 0  # Initialize ranks to 0

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            # Path-Compression, set to grand-parent//not always reqd T -> O(logn)
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:  # If same root parent
            return False

        if (
            self.rank[p1] > self.rank[p2]
        ):  # Check for rank(height), larger rank node is parent
            self.parent[
                p2
            ] = p1  # Rank won't update, as child node will be same as other child nodes
        elif (
            self.rank[p1] < self.rank[p2]
        ):  # Check for rank(height), larger rank node is parent
            self.parent[
                p1
            ] = p2  # Rank won't update, as child node will be same as other child nodes
        else:
            self.parent[
                p1
            ] = p2  # Add a new child, new layer, so rank of parent would change

            self.rank[p2] += 1

        return True

        # Path-compression and find-by-rank, -> T(Inverse Ackermann function (delta n)) -> O(1)
