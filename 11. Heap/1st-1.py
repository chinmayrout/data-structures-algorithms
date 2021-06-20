# Min-Heap
# https://www.geeksforgeeks.org/min-heap-in-python/
'''
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than
 or equal to the values in the children of that node. 
Mapping the elements of a heap into an array is trivial: if a node is stored at index k,
 then its left child is stored at index 2k + 1 and its right child at index 2k + 2.
'''
import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return pos//2

    # Function to return the position of the left child for the node currently at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of the right child for the node currently at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fPos, sPos):
        self.Heap[fPos], self.Heap[sPos] = self.Heap[sPos], self.Heap[fPos]

    # Function to heapidfy the node as pos
    def minHeapify(self, pos):
        # If the node is a non-leaf node and greater than any of it's child
        if not self.isLeaf(pos):
            if(self.Heap[pos] > self.Heap[self.leftChild(pos)] or self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                # Swap with the left child and heapify the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    
    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        
        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    
    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))


    # Function to build the min heap using the minHeapify function
    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    # Function to remove and return the minimum element from the heap
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
 
# Driver Code
if __name__ == "__main__":
     
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
 
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))