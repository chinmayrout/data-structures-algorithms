# Pre-order, Inorder, Post-Order Traversal of a tree both using recursion

# Data structure to store a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function to perform pre-order traversal on the tree
def preorder(root): # root -> left -> right
    # return if the current node is empty
    if root is None:
        return

    # Display the data part of the root (or current node)
    print(root.data, end = ' ')

    # Traverse the left subtree
    preorder(root.left)

    # Traverse the right subtree
    preorder(root.right)



# Recursive function to perform inorder traversal on the tree
def inorder(root):  # left -> root -> right
    # return if the current node is empty
    if root is None:
        return

    # Traverse the left subtree
    inorder(root.left)

    # Display the data part of the root (or current node)
    print(root.data, end = ' ')

    # Traverse the right subtree
    inorder(root.right)


def postorder(root):    # left -> right -> root
    # return if current node is empty
    if root is None:
        return

    # Traverse the left subtree
    postorder(root.left)

    # Traverset the right subtree
    postorder(root.right)

    # Display the data part of the root (or current node)
    print(root.data, end = ' ')


if __name__ == '__main__':
    '''
    Construct the following tree
                    1
                   / \
                  2   3
                /  \
               4    5
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder (Root->Left->Right)")
    preorder(root)
    print("\nInorder (Left->Root->Right)")
    inorder(root)
    print("\nPostorder (Left->Right->Root)")
    postorder(root)