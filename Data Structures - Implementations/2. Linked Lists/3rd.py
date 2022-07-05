# 3. Insertion in a Linked List

# a. Insert at the beginning of a Linked List
# b. Insert at the end of a Linked List
# c. Insert in the middle of a Linked List
# d. Inserting in between two Data Nodes

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_end(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def insert_middle(self, value, position):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        index = 1
        current = self.head
        while index < position:
            current = current.next
            index += 1

        node.next = current.next
        current.next = node


llist = LinkedList()
llist.head = Node("Mon")


node1 = Node("Tue")
node2 = Node("Wed")
node3 = Node("Thu")
node4 = Node("Fri")
node5 = Node("Sat")
node6 = Node("Sun")


# Link first node to second node
llist.head.next = node1

# link second node to third node
node1.next = node2

# link third node to fourth node
node2.next = node3

# link fourth node to fifth node
node3.next = node4

# link fifth node to sixth node
node4.next = node5

# link sixth node to seventh node
node5.next = node6

# link seventh node to None
node6.next = None

llist.listprint()


llist.insert_beginning("Mon")
llist.listprint()

llist.insert_beginning("Tue")
llist.listprint()

llist.insert_middle("Wed", 3)
llist.listprint()
