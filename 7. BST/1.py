# Find a value in a BST - Searching and inserting(insert values which get sorted so that the tree remains a bst)
'''
Binary Search Tree is a node-based binary tree data structure which has the following properties:  

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree. 
There must be no duplicate nodes.
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def searchBST(root, data):
    while root is not None and root.data != data:

        if data < root.data:        # root = root.left if data < root.data else root.right
            root = root.left
        else:
            root = root.right
    return root


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# Adding the general way
# root = Node(1)
# root.left = Node(3)
# root.left.left = Node(1)
# root.left.right = Node(6)
# root.left.right.left = Node(4)
# root.left.right.right = Node(7)
# root.right = Node(10)
# root.right.right = Node(14)
# root.right.right.left = Node(13)

root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

'''
        50
       /  \
      30   70
     /  \  / \
    20  40 60 80
'''

print(searchBST(root, 15))
print(searchBST(root, 14))

inorder(root)