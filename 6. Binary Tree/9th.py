# Left View of a Tree

# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function to print left view of a binary tree
def leftViewUtil(root, level, max_level):
    # Base Case
    if root is None:
        return

        # If this is the first node of its level
    if(max_level[0] < level):
        print(root.data)
        max_level[0] = level

        # Recur for left and right subtree
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)

# A wrapper over leftViewUtil()
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)

#=========================================================================
# Iterative way
def leftViewUtil1(root, q):
    if root == None:
        return

    # Append Root
    q.append(root)

    # Delimiter
    q.append(None)

    while(len(q)):
        temp = q[0]

        if temp:

            # Prints first node of each level
            print(temp.data, end = ' ')

            # Append children of all nodes at current level
            while(q[0] != None):
                temp = q[0]

                # If left child is present append into queue
                if temp.left:
                    q.append(temp.left)

                # If right child is present append into queue
                if temp.right:
                    q.append(temp.right)

                # Pop the current node
                q.pop(0)
                
            # Append delimiter for the next level
            q.append(None)

        # pop the delimiter of the previous level
        q.pop(0)


def leftView1(root):
    #Queue to store all the nodes of the tree
    q = []
    leftViewUtil1(root, q)


#Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.left.right = Node(6)
root.right.left.right.left = Node(7)
root.right.left.right.right = Node(8)
 
leftView(root)      #Recursive
leftView1(root)     #Iterative

