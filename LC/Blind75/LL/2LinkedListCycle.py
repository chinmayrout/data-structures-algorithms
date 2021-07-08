'''
psuedo-code

def hasCycle(self, head):
    if head is None:
        return False

    slow_p = head
    fast_p = head.next

    while(fast_p != slow_p):
        if fast_p is None or fast_p.next is None:
            return False

        slow_p = slow_p.next
        fast_p = fast_p.next.next


    # if loop exists
    if slow_p == fast_p:
        return True
    else:
        return False
        
'''