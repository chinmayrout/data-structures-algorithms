# DFS - Preorder, Inorder, Postorder Iterative

from collections import deque

# Data structure to store binary tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative function to perfrom preorder traversal on the tree


def preorderIterative(root):
    # return if the tree is empty
    if root is None:
        return

    # Create an empty stack and push the root node
    stack = deque()
    stack.append(root)

    # Start from the root node (set current node to the root node)
    curr = root

    # Loop till stack is empty
    while stack:
        # if the current node exists, print it and push it's right child to the stack before moving to it's left child
        if curr:
            print(curr.data, end=' ')

            if curr.right:
                stack.append(curr.right)

            curr = curr.left

        # is the current node is None, pop a node from the stack
        # set the current node to the popped node

        else:
            curr = stack.pop()


# Iterative function to perform inorder traversal on the tree
def inorderIterative(root):  # Left->Root->Right
    # return if the tree is empty
    if root is None:
        return
    # create an empty stack
    stack = deque()

    # start from root node (set current node to the root node)
    curr = root

    # if current node is None and stack is also empty, we are done
    while stack or curr:

        # if the current node exists, push it into the stack (defer it) and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # print it, and finally set the current node to it's right child
            curr = stack.pop()
            print(curr.data, end=' ')

            curr = curr.right


# Iterative function to perfrom postorder traversal on the tree
def postorderIterative(root):  # Left->Right->Root
    # return if the tree is empty
    if root is None:
        return

    # create an empty stack
    stack = deque()

    while(True):
        while(root != None):
            stack.append(root)
            stack.append(root)
            root = root.left

        # Check for empty stack
        if (len(stack) == 0):
            return

        root = stack.pop()

        if(len(stack) > 0 and stack[-1] == root):
            root = root.right

        else:
            print(root.data, end=" ")
            root = None


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
    preorderIterative(root)
    print("\nInorder (Left->Root->Right)")
    inorderIterative(root)
    print("\nPostorder (Left->Right->Root)")

    postorderIterative(root)
