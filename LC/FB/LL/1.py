# https://leetcode.com/problems/add-two-numbers


'''
The steps are: 
1. Traverse the two linked lists from start to end
2. Add the two digits each from respective linked lists.
3. If one of the lists has reached the end then take 0 as its digit.
4. Continue it until both the end of the lists.
5. If the sum of two digits is greater than 9 then set carry as 1 and the current digit as sum % 10
'''

class Node:
    # Constructor to initialize the node object
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
        new_node.next = self.head
        self.head = new_node

    # Add contents of two linked-lists and return the head node of the resultant list
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # While both list exists
        while(first is not None or second is not None):
            # Calculate the value of next digit in resultant list
            # The next digit is tum of following things
            # i. Carry
            # ii. Next digit of first list(if there is a next digit)
            # iii. Next digit of second list (if there is a next digit)

            fData = 0 if first is None else first.data
            sData = 0 if second is None else second.data
            Sum = carry + fData + sData

            # Update carry for next calculation
            carry = 1 if Sum >=10 else 0

            # Update sum if it is greater than 10
            Sum = Sum if Sum <10 else Sum % 10

            # Create a new node with sum as data
            temp = Node(Sum)

            # If this is the first node then set it as head of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



# Driver Code
first = LinkedList()
second = LinkedList()
 
# Create first list
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print("First List is ")
first.printList()
 
# Create second list
second.push(4)
second.push(8)
print("\nSecond List is ")
second.printList()

# Add the two lists and see result
res = LinkedList()
res.addTwoLists(first.head, second.head)
print("\nResultant list is ")
res.printList()
 