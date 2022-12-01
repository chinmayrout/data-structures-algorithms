# Bellman Ford
"""
Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.
It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.


How it works?
Bellman Ford algorithm works by overestimating the length of the path from the starting vertex to all other vertices. 
Then it iteratively relaxes those estimates by finding new paths that are shorter than the previously overestimated paths.
By doing this repeatedly for all vertices, we can guarantee that the result is optimized.

PsuedoCode
1. We need to maintain the path distance of every vertex. We can store that in an array of size v, where v is the number of vertices.
2. We also want to be able to get the shortest path, not only know the length of the shortest path. For this, we map each vertex to the vertex that last updated its path length.
3. Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.

"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Total number of vertices(node) in the graph
        self.graph = []  # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        # Step1: Fill the distance array and predecessor array
        dist = [float("inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step2: Relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[d] + w

        # Step 3: Detect negative cycle, if value changes then we have a negative cycle in
        # the graph and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)


"""
Q1. Why do we need to be careful with negative weights?
Ans - Negative weight edges can create negative weight cycles i.e. a cycle that will reduce the total path distance by coming back to the same point.
negative weight cycles can give an incorrect result when trying to find out the shortest path
Negative weight cycles can give an incorrect result when trying to find out the shortest path
Shortest path algorithms like Dijkstra's Algorithm that aren't able to detect such a cycle can give an incorrect result because they can go through a negative weight cycle and reduce the path length.

Q2. Why would one ever have edges with negative weights in real life?
Ans- Negative weight edges might seem useless at first but they can explain a lot of phenomena like cashflow, the heat released/absorbed in a chemical reaction, etc.
    For instance, if there are different ways to reach from one chemical A to another chemical B, each method will have sub-reactions involving both heat dissipation and absorption.
    If we want to find the set of reactions where minimum energy is required, then we will need to be able to factor in the heat absorption as negative weights and heat dissipation as positive weights.

Q3. Bellman Ford vs Dijkstra
Ans - Bellman Ford's algorithm and Dijkstra's algorithm are very similar in structure. 
While Dijkstra looks only to the immediate neighbors of a vertex, Bellman goes through each edge in every iteration.



Time Complexity
Best Case Complexity        O(E)
Average Case Complexity 	O(VE)
Worst Case Complexity		O(VE)
		
Space Complexity is O(V).


Bellman Ford's Algorithm Applications

    1. For calculating shortest paths in routing algorithms
    2. For finding the shortest path

"""
