#LinkedList Inserting a Node


#node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked List class contains a Node object
class LinkedList:

    #Function to initialize head
    def __init__(self):
        self.head = None

    #Function to insert a new node at the beginning
    def push(self, new_data):

        # 1 & 2: Allocate the node and push the data
        new_node = Node(new_data)
        #3: Make next of new node as head
        new_node.next = self.head
        #4: Move the head to point to new node
        self.head = new_node

    #Insert a new node after given prev_node
    def insertAfter(self, prev_node, new_data):     #Visualize
        #1. Check if given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        # 2. Create new node & Put in the data
        new_node = Node(new_data)
        #3. Make next of new node as next of prev_node
        new_node.next = prev_node.next
        # 4. Make next of prev_node as new_node
        prev_node.next = new_node

    #Append a new node in the end
    def append(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If linkedlist is empty, then make the new node as head
        if self.head = None:


