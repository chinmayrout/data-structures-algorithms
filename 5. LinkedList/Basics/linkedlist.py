#Linkedlist with traversal

class Node:

    #Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked List class contains a Node Object
class LinkedList:
    #Function to initialise head

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# Code execution starts here
if __name__ == '__main__':
    #Start with empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()