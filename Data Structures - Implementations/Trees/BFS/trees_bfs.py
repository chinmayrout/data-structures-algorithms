# Level order traversal
# Given a binary tree, find its level order traversal.
# Level order traversal of a tree is breadth-first traversal for the tree.

# Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
# It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]),
# and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
# https://en.wikipedia.org/wiki/Breadth-first_search

# Using queue

class Node:
    # A utility function to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative method to print the height of binary tree


def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
        # Prints front of the queue and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is - ")
printLevelOrder(root)
