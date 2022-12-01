# Union-Find Data Structure(A.K.A Disjoint Set Data Structure)
# A tree-DS but usally used in Graph
# We have disjoint sets, eg -> two graphs
# Can be used to count the number of connected components
# Can also be used for cycle detection

# DFS can solve this problem, but sometimes UF is better

# Union find is basically a forest of trees

# Start with individual node and make each node it's parent
# Take a node and set is as parent of another node which it has an edge with (arbitrary)
# Go to root of each tree and union with another tree
#
# Union by rank(height) -> Take smaller height tree and add to larger height tree
# If root of two nodes are the same, they are part of same connected component,
# We can't union in this case as they are part of same set, return False for union in this case, graph has cycle


# Union-find doesn't accurately represent the graph,
# it's about finding cycles and count number of connected components


class UnionFind:
    def __init__(self, n):  # Constructor takes size of the set
        self.parent = {}  # for taking parents of every node
        self.rank = {}  # track of rank(height) of each node

        for i in range(1, n + 1):  # start from 1
            self.parent[i] = i  # initialize parent to itself
            self.rank[i] = 0  # initialize the rank to 0

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[
                self.parent[p]
            ]  # path-compression, set to grand-parent//not always reqd T-> O(logn)
            p = self.parent[p]

        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:  # if same root parent
            return False

        if (
            self.rank[p1] > self.rank[p2]
        ):  # check for rank(height), larger rank node is the parent
            self.parent[
                p2
            ] = p1  # rank won't change as child node will be at same level as other child nodes

        elif (
            self.rank[p1] < self.rank[p2]
        ):  # check for rank(height), larger rank node is the parent
            self.parent[
                p1
            ] = p2  # rank won't change as child node will be at same level as other child nodes

        else:
            self.parent[
                p1
            ] = p2  # add a new child, new layer, so rank of parent would change
            self.rank[p2] += 1
        return True

        # Path-compression and find-by-rank, -> T(Inverse Ackermann function (delta n)) -> O(1)
