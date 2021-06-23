# Merge Sort For Linked lists.[Very Important]
# https://www.geeksforgeeks.org/merge-sort-for-linked-list/



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    # Function to insert a new Node at the beginnning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def mergeSort(self, head):
        if head.next == None:
            return head
        
        mid = self.findMid(head)
        head2 = mid.next
        mid.next = None
        newHead1 = self.mergeSort(head)
        newHead2 = self.mergeSort(head2)
        finalHead = self.merge(newHead1, newHead2)

        return finalHead

    def findMid(self, head):
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, head1, head2):
        merged = Node(-1)
        temp = merged

        while(head1 != None and head2 != None):
            if(head1.data < head2.data):
                temp.next = head1
                head1 = head1.next

            else:
                temp.next = head2
                head2 = head2.next

            temp = temp.next


        while head1 != None:
            temp.next = head1
            head1 = head1.next
            temp = temp.next
        
        while head2 != None:
            temp.next = head2
            head2 = head2.next
            temp = temp.next

        return merged.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



# Driver Code
llist = Linkedlist()
llist.push(7)
llist.push(10)
llist.push(5)
llist.push(20)
llist.push(3)
llist.push(2)

print ("Created Linked List: ")
llist.printList()

llist.head = llist.mergeSort(llist.head)
print("Merge Sort on Linked-List")
llist.printList()


'''
mergeSort():

If the size of the linked list is 1 then return the head
Find mid using The Tortoise and The Hare Approach
Store the next of mid in head2 i.e. the right sub-linked list.
Now Make the next midpoint null.
Recursively call mergeSort() on both left and right sub-linked list and store the new head of the left and right linked list.
Call merge() given the arguments new heads of left and right sub-linked lists and store the final head returned after merging.
Return the final head of the merged linkedlist.
merge(head1, head2):

Take a pointer say merged to store the merged list in it and store a dummy node in it.
Take a pointer temp and assign merge to it.
If the data of head1 is less than the data of head2, then, store head1 in next of temp & move head1 to the next of head1.
Else store head2 in next of temp & move head2 to the next of head2.
Move temp to the next of temp.
Repeat steps 3, 4 & 5 until head1 is not equal to null and head2 is not equal to null.
Now add any remaining nodes of the first or the second linked list to the merged linked list.
Return the next of merged(that will ignore the dummy and return the head of the final merged linked list)


Time Complexity: O(n*log n)

Space Complexity: O(log n)
'''