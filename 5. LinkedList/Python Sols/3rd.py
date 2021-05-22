# Write a program to Detect loop in a linked list.
# Floyd’s Cycle-Finding Algorithm 

# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
# Traverse linked list using two pointers.
# Move one pointer(slow_p) by one and another pointer(fast_p) by two.
# If these pointers meet at the same node then there is a loop. 
# If pointers do not meet then linked list doesn’t have a loop.
#codingninjas.com/blog/2020/09/09/floyds-cycle-detection-algorithm/

# Node Class
class Node:
    # Constructor to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head   # changing next-pointer of new_node to head pointer
        self.head = new_node        # changing head pointer to the new_node

    #Utility function to print the linkedlist
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    #AlGO - FLoyd's cycle-finding algo
    def detectLoop(self):
        if self.head is None:
            return False
        if self.head.next is None:
            return False
        slow_p = self.head
        fast_p = self.head
        # Move slow and fast 1 and 2 steps respectively
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        # while (slow_p and fast_p and fast_p.next):
        #     slow_p = slow_p.next
        #     fast_p = fast_p.next.next
        #     if slow_p == fast_p:
        #         return 

        # Search for loop using slow and fast pointers
        while (fast_p is not None and slow_p is not None):
            if fast_p.next is None:
                break
            if slow_p == fast_p:
                break
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # if loop exists
        if slow_p == fast_p:
            return True


# Driver Code for the program
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(3)

#understanding linkedlist
#print(llist.head.data)


# Create a loop for testing
# llist.head.next.next.next = llist.head
if (llist.detectLoop()):
    print("Found loop")

else:
    print("No loop")

llist.printList()


