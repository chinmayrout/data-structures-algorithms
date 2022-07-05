class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        if not self.head:
            self.head = Node(data)
            self.head.next = self.head

        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):

        current = self.head
        while self.head:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def prepend(self, data):

        new_node = Node(data)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node

        else:
            while current.next != self.head:
                current = current.next

            current.next = new_node
        self.head = new_node

    def remove(self, key):

        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        else:
            current = self.head
            previous = None

            while current.next != self.head:
                previous = current
                current = current.next

                if current.data == key:
                    previous.next = current.next
                    current = current.next

    def __len__(self):

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

            if current == self.head:
                break
        return count

    def split_list(self):

        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid_point = size // 2
        count = 0
        previous = None
        current = self.head

        while current and count < mid_point:
            count += 1
            previous = current
            current = current.next

        print("Count", count)
        print("Current Node:", current.data)
        print("Previous Node:", previous.data)
        previous.next = self.head

        # Create second list
        split_cllist = CircularLinkedList()

        while current.next != self.head:
            split_cllist.append(current.data)
            current = current.next

        split_cllist.append(current.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    def remove_node(self, node):

        if self.head == node:
            current = self.head

            while current.next != self.head:
                current = current.next
            current.next = self.head.next

            self.head = self.head.next

        else:
            current = self.head
            previous = None

            while current.next != self.head:
                previous = current
                current = current.next

                if current == node:
                    previous.next = current.next
                    current = current.next

    def josephus_circle(self, step):

        current = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                current = current.next
                count += 1
            print("Removed: ", str(current.data))
            self.remove_node(current)
            current = current.next

    def Is_circular_linked_list(self, input_list):
        pass


cllist = CircularLinkedList()
cllist.append("1")
cllist.append("2")
cllist.append("3")
cllist.append("4")
