# Validate Binary Search Tree
'''
A binary search tree (BST) is a node based binary tree data structure which has the following properties. 
• The left subtree of a node contains only nodes with keys less than the node’s key. 
• The right subtree of a node contains only nodes with keys greater than the node’s key. 
• Both the left and right subtrees must also be binary search trees.
From the above properties it naturally follows that: 
• Each node (item in the tree) has a distinct key.
'''



# A binary tree node containing data field, left and right pointers
class Node:
    # Constructor to create new node
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isBSTUtil(root, prev):
    # Traverse the tree in inorder fashion and keep track of prev node
    if root != None:
        if not isBSTUtil(root.left, prev):
            return False
        
        # Allows only distinct valued nodes
        if prev!= None and root.data <= prev.data:
            return False

        prev = root

        return isBSTUtil(root.right, prev)

    return True

def isBST(root):
    prev = None
    return isBSTUtil(root, prev)

# Driver Code
if __name__== '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(15)
    root.left.left = Node(1)
    root.left.right = Node(4)
    # root.right.left = Node(1)
    #root.right.right = Node(4)
    #root.right.left.left = Node(40)


    if isBST(root) == None:
        print("isBST")

    else:
        print("Not a BST")