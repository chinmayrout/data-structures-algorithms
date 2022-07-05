# 1. Creation of Linked list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


llist = LinkedList()
llist.head = Node("Mon")

node1 = Node("Tue")
node2 = Node("Wed")

# Link first node to second node
llist.head.next = node1

# link second node to third node
node1.next = node2
