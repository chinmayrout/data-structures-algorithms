# Create a Graph and print it
# https://www.geeksforgeeks.org/graph-and-its-representations/
# A python program to demonstrate the adjacency list representation of the graph
# important code - must practices

# A class to represent the adjacency list of the node
class ADJNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph is the list of the adajcency lists. 
# Size of the arrayw will be the number of the verices "V"

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V


    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source code
        node = ADJNode(dest)            # Making a node with data = dest,
        node.next = self.graph[src]     # assigning next pointer to the list graph in src
        self.graph[src] = node          # making the graph[src] become node, so in future next element with same src gets added here

        # Adding the source code node to the destination as it is the undirected graph
        node = ADJNode(src)             # making a node with data = src
        node.next = self.graph[dest]    # assigning next pointer to the list graph in dest
        self.graph[dest] = node         # making the graph[dest] become node, so in futute next element with same dest gets added

    
    # A function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency List of Vertex {}\n head".format(i), end = "")
            temp = self.graph[i]        # next pointer in node is stored to previous element s
            while temp:
                print(" -> {}".format(temp.vertex), end = "")
                temp = temp.next

            print("\n")



# Driver Code
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0,1)
    graph.add_edge(0,4)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,3)
    graph.add_edge(3,4)

    graph.print_graph()
