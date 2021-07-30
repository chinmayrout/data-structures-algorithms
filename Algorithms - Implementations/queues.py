# First In First Out (FIFO) manner.
# https://www.geeksforgeeks.org/queue-in-python/
# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)

#==============================================================================================================================
# using list - slower - uses O(n)
# instead of enqueue use append() and for dequeue use pop() 

queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial Queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)


#==============================================================================================================================
# using collections.dequeue - fast - O(1)

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)


#==============================================================================================================================
# queue using queue.Queue
# 
# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

from queue import Queue

# Initialize a queue
q = Queue(maxsize = 3)

# qsize() gives the maxsize of the Queue
print(q.qsize())

# Adding of elements to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full Queue
print("\nFull:", q.full())

# Removing element from Queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for empty
# Queue
print("\nEmpty:", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
#==============================================================================================================================
#==============================================================================================================================
#==============================================================================================================================
#==============================================================================================================================
#==============================================================================================================================
