# Write a Program to Find the Maximum Depth or Height of a Tree
# https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/


# A binary tree node
class Node:
    # A contructor to create a new-node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
# Compute the "maxDepth" of a tree -- the number of nodes along the longest path from the root down 
# to the farthest leaf node

def maxDepth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        ldepth = maxDepth(node.left)
        rdepth = maxDepth(node.right)

        #Use the larger one
        if ldepth > rdepth:
            return ldepth + 1

        else:
            return rdepth + 1

# Driver Code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Height of tree is %d" %(maxDepth(root)))
# Time Complexity: O(n) 
# =================================================================================================

# Iterative Pending - https://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/