# Write a program to Delete loop in a linked list.
# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
# This method is also dependent on Floyd’s Cycle detection algorithm.
# Detect Loop using Floyd’s Cycle detection algorithm and get the pointer to a loop node.
# Count the number of nodes in loop. Let the count be k.
# Fix one pointer to the head and another to a kth node from the head.
# Move both pointers at the same pace, they will meet at loop starting node.
# Get a pointer to the last node of the loop and make next of it as NULL.

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize the head
    def __init__(self):
        self.head = None

    # Function to insert a new node in the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head   # changing next-pointer of new_node to head pointer
        self.head = new_node        # changing head pointer to new_node

    # Utility to print the linked-List
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Floyd's Algo to detect and remove a loop in the linked-list
    def detectAndRemove(self):

        if self.head is None:
            return

        if self.head.next is None:
            return

        slow = self.head
        fast = self.head

        # Move slow and fast 1 and 2 steps respectively
        slow = slow.next
        fast = fast.next.next

        # Search for loop using slow and fast pointers
        while(fast is not None):
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        # if loop exists
        if slow == fast:
            slow = self.head
            while(slow.next != fast.next):
                slow = slow.next
                fast = fast.next

            # Since fast.next is the looping point
            fast.next = None        # Removed Loop


        
# Driver Program

llist = LinkedList()
print("Hello")
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)

#Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemove()

print("Linked-List after removing Loop!")
llist.printList()