#  Find the starting point of the loop. 
# https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/

class Node:
    # Constructor to initialize the Node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert new node in the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Utility to print the linked-list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        if(self.head == None or self.head.next == None):
            return None

        slow = self.head
        fast = self.head

        #Move slow and fast 1 and 2 steps ahead respectively
        slow = slow.next
        fast = fast.next.next

        # Search for loop using slow and fast pointers
        while(fast and fast.next):
            if slow == fast:
                break

            slow = slow.next
            fast = fast.next.next


        # If loops doesn't exist
        if slow != fast:
            return None

        # If loop exists. Start slow from head and fast from meeting point
        slow = self.head

        while(slow != fast):
            slow = slow.next
            fast = fast.next

        return slow


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(50)
    llist.push(20)
    llist.push(15)
    llist.push(4)
    llist.push(10)
    
    #Create a a loop for nesting
    llist.head.next.next.next.next.next = llist.head.next.next

    res = llist.detectLoop()

    if res == None:
        print("Loop doesn't exist")

    else:
        print("Loop starting node is:"+ str(res.data))