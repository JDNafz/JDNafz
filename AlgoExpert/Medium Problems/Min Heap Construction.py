'''
Write the definitions for the methods to a MinHeap class 
- build it from an array of integers
- insert
- remove the min value
- peek at rootvalue
- sift integers up and down
*the heap lives in the form of an array at all times. 

🔵 Medium
https://www.algoexpert.io/questions/min-heap-construction
'''




# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array): #constructor
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.lastParent = None
    def buildHeap(self,array):
        self.heap = array
        x = len(self.heap) - 1
        print(x)
        parentIdx = self.getParentIdx(x)
      
        self.lastParent = parentIdx
        for i in range(parentIdx,-1,-1):
            self.siftDown(i)
        return self.heap 

    def siftDown(self, currentIdx):

        child1Idx = self.getChild1Idx(currentIdx)
        child1 = self.heap[child1Idx]

        child2Idx = self.getChild2Idx(currentIdx)
        if child2Idx > len(self.heap)-1:
            child2 = float("inf")
        else:
            child2 = self.heap[child2Idx]
        while self.heap[currentIdx] > child1 or self.heap[currentIdx] > child2:
            if child1 <= child2:
                self.heap[child1Idx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[child1Idx]
                currentIdx = child1Idx
            else:
                self.heap[child2Idx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[child2Idx]
                currentIdx = child2Idx
            child1Idx = self.getChild1Idx(currentIdx)
            if child1Idx > len(self.heap)-1:
                child1 = float("inf")
            else:
                child1 = self.heap[child1Idx]
            child2Idx = self.getChild2Idx(currentIdx) 
            if child2Idx > len(self.heap)-1:
                child2 = float("inf")
            else:
                child2 = self.heap[child2Idx]

            #print after each run through siftDown
            # print(self.heap)

    def siftUp(self, currentIdx, parentIdx):
        while self.heap[currentIdx] < self.heap[parentIdx]:
            self.heap[currentIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currentIdx]
            currentIdx = parentIdx
            parentIdx = self.getParentIdx(parentIdx)
            

    def peek(self):
        return self.heap[0]

    def remove(self):
        currentIdx = len(self.heap) - 1
        self.heap[0], self.heap[currentIdx] = self.heap[currentIdx], self.heap[0]
        self.siftDown(0)
        popped = self.heap.pop(currentIdx)
        return popped

    def insert(self, value):
        currentIdx = len(self.heap)
        self.heap.append(value)
        parentValue = self.getParentValue(currentIdx)
        parentIdx = self.getParentIdx(currentIdx)
        if value < parentValue:
            self.siftUp(currentIdx, parentIdx)
    
    def getParentValue(self, currentIdx):
        parentIdx = self.getParentIdx(currentIdx)
        parentValue = self.heap[parentIdx]
        return parentValue


    def getParentIdx(self, currentIdx):
        return (currentIdx - 1) // 2
        

    def getChild1Idx(self, currentIdx):
        return (2 * currentIdx) + 1
    def getChild2Idx(self, currentIdx):
        return (2 * currentIdx) + 2


# heapBoi = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
# heapGurl = MinHeap([100,50,25,10,3,7])
# print(heapBoi.heap)

# heapBoi.insert(76)
# heap.insert(87)

# array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
# value = 76
