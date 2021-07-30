# https://www.geeksforgeeks.org/stack-in-python/
# Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner
# using list

stack = []

# append() function to push element in the stack

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)

# pop() function to pop element from stack in LIFO order
print('\nElements popped out of stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)



#==========================================================================

# Python Stack can also be implemented using double ended queue(deque) from collections module.
# Dequeue is preferred over list in cases where we need quicker append and pop operations
# Dequeue takes O(1) compared to O(n) in list

from collections import deque

stack = deque()

# append() function to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)


# pop() function to pop element from stack in LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\n Stack after elements are poped:')
print(stack)