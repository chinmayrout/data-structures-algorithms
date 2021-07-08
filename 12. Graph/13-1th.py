# Kahn's Algorithm for Topological Sorting
# There can be more than one topological sorting for a graph. 

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency list
        self.V = vertices           # No. of vertices


    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do Topological Sort.
    def topologicalSort(self):
        # Create a vector to store indegrees of all vertices.
        # Initialize all indegrees as 0
        in_degree = [0] *(self.V)

        # Traverse adjacency lists to fill indegrees of vertices. This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1


        # Create an queue and enqueue all vertices with indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result(A topological ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue adjacents if indefree of adjacent becomes 0
        while queue:
            # Extract front of queue(or perform dequeue) and add it to topological order
            u = queue.pop(0)
            top_order.append(u)


            # Iterate through all neighboring nodes of dequeued node u and decrease their in-degree by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # if in-degree becomes zero, add it to the queue
                if in_degree[i] ==0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt!= self.V:
            print("There exists a cycle in the graph")

        else:
            print(top_order)
        

# Driver Code
g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print("Following is a Topological Sort of the given graph")
g.topologicalSort()


'''
Time Complexity: O(V+E). 
The outer for loop will be executed V number of times and the inner for loop will be executed E number of times.
Auxillary Space: O(V). 
The queue needs to store all the vertices of the graph. So the space required is O(V)
'''
