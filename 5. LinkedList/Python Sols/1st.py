#Write a Program to reverse the Linked List. (Both Iterative and recursive)
# https://www.geeksforgeeks.org/reverse-a-linked-list/
# Iterative Approach

'''
1. Initialize three pointers prev as NULL, curr as head and next as NULL.
2. Iterate through the linked list. In loop, do following. 
// Before changing next of current, 
// store next node 
next = curr->next
// Now change next of current 
// This is where actual reversing happens 
curr->next = prev 
// Move prev and curr one step forward 
prev = curr 
curr = next

'''

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
        while(current is not None):         # main goal is to point head.next to prev node
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



#================================================================================
# Recursive Approach
'''
1) Divide the list in two parts - first node and rest of the linked list.
2) Call reverse for the rest of the linked list.
3) Link rest to first.
4) Fix head pointer
'''

class Node1:

