class ListNode:
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self) -> ListNode:

        current = self.head
        prev = None
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next


            next = current.next

        return prev

    def printList(self):
        temp = self.data
        while temp:
            print(temp.data)

# Driver Code
s =Solution()
a = ListNode(1)