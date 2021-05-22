# Reverse a Linked List in group of Given Size. [Very Imp]
# https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
# Given a linked list, write a function to reverse every k node


#Node Class
class Node:

    #Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        if head == None:
            return None
        current = head
        prev = None
        next = None
        count = 0

        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count +=1

        # next is now a pointer to (k+1)th node
        # recursively  call for the list starting from current. 
        # Make the rest of the list as next of first node

        if next is not None:
            head.next = self.reverse(next, k)

        #prev is new head of the input list
        return prev


    #Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Print utility
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

#Driver Code
llist = LinkedList()
llist.push(100)
llist.push(200)
llist.push(300)
llist.push(400)
llist.push(500)
llist.push(600)
llist.push(700)

print("Given List is: \n")
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print("Reversed linkedList: \n")
llist.printList()




