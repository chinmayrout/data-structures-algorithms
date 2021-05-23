# Reverse Level Order Traversal 
# https://www.geeksforgeeks.org/reverse-level-order-traversal/


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Function to print reverse level order traversal
def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1, h+1)):
        printGivenLevel(root, i)

# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)

    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

# Compute the height of a tree-- the number of nodes along the longest path
#  from the root node down to the farthest leaf node

def height(node):
    if node is None:
        return 0
    else:

        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

#Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree:")
reverseLevelOrder(root)

# Time Complexity = O(n2)


# =================================================================================================
#Using Stack and Queue

from collections import deque

# using Node class from the recursive code

# Given a binary tree, print it's node in reverse order

def reverseLevelOrderIterative(root):
    # We can use a double ended queue which provides O(1) insert at beginning using the appendleft method
    # We do the regular level order traversal but instead of processing the left child we first process the right child
    # first and then we process the left child first we process the right child first and then we process the left child 
    # of the current node

    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue

        ans.appendleft(node.data)

        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

        print(ans)

# Driver Code
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

print("Level Order Traversal of Binary Tree is:")
reverseLevelOrderIterative(root1)