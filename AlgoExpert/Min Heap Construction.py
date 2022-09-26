# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self,array):
        parentNodeList = getParents(array)
        for i in range(len(array)):
            heap.siftDown(i,array)

    def siftDown(self, currentIdx, array):
        child1 = getChild1Idx(currentIdx)
        child2 = getChild2Idx(currentIdx)
        while array[currentIdx] > array[child1] and value > array[child2]:
            if array[child1] < array[child2]:
                array[child1], array[currentIdx] = array[currentIdx], array[child1]
                currentIdx = child1
            else:
                array[child2], array[currentIdx] = array[currentIdx], array[child2]
                currentIdx = child2
            child1 = getChild1Idx(currentIdx)
            child2 = getChild2Idx(currentIdx)

    def siftUp(self, currentIdx, parentIdx, array):
        while array[currentIdx] < array[parentIdx]:
            array[currentIdx], array[parentIdx] = array[parentIdx], array[currentIdx]
            currentIdx = parentIdx
            parentIdx = getParentIdx(parentIdx)
            
            # 

    def peek(self):
        # Write your code here.
        pass

    def remove(self, array):
        currentIdx = len(array) - 1
        array[0], array[currentIdx] = array[currentIdx], array[0]
        heap.siftDown(0,array)
        popped = array.pop(currentIdx)
        return popped

    def insert(self, value, array):
        currentIdx = len(array)
        array.append(value)
        parentValue = getParentValue(currentIdx)
        parentIdx = getParentIdx(currentIdx)
        if value < parentValue:
            heap.siftup(currentIdx, parentIdx, array)

def getParents(array):
    parentNodes = []
    lastchild = len(array) - 1
    parent = getParentIdx(lastChild) 
    return parentNodes

def getParentIdx(currentIdx):
    return (currentIdx - 1) // 2
     
def getParentValue(currentIdx):
    parentIdx = getParentIdx(currentIdx)
    parentValue = array[parentIdx]
    # print(parentValue, "idx:",parentIdx)
    return parentValue

def getChild1Idx(currentIdx):
    return (2 * currentIdx) + 1
def getChild2Idx(currentIdx):
    return (2 * currentIdx) + 2


heap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
heap.insert(76)
# heap.insert(87)

array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
value = 76
