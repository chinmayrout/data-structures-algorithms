#Write a Program to reverse the Linked List. (Both Iterative and recursive)

# Iterative Approach

# Linked-List Node
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Create and handle list operations
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linkedlist - iterative
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev     #Main Algo
            prev = current
            current = next

        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Utility to print the linked-list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


#Driver Code
llist = LinkedList()
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)

print("Given Linked List: ")
llist.printList()
llist.reverse()
print("\nReversed List: ")
llist.printList()

# Time Complexity: O(n) 
# Space Complexity: O(1)



#TODO: Recursive Approach
