# 4. Removing a node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove_node(self, remove_key):
        head = self.head

        if head is not None:
            if head.data == remove_key:
                self.head = head.next
                head = None
                return

        while head is not None:
            if head.data == remove_key:
                break
            prev = head
            head = head.next

        if head is None:
            return
