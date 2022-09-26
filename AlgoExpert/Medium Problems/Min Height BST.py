
'''
construct a BST, with the shortest possible depth, from a sorted array

🔵 Medium
https://www.algoexpert.io/questions/min-height-bst






O(nlog(n)) time | O(n) space
nlog(n) because of the use of the insert method being called on the root every time

def minHeightBst(array):
    return buildMinHeightBst(array,None, 0, len(array)-1)


def buildMinHeightBst(array, bst, start, end):    
    if start > end:
        return
    mid = (start + end) // 2
    if bst is None:
        bst = BST(array[mid])
    else:
        bst.insert(array[mid])
    buildMinHeightBst(array, bst, start, mid -1)
    buildMinHeightBst(array, bst, mid + 1, end)
    return bst

'''

def minHeightBst(array):
    return buildMinHeightBst(array, 0, len(array)-1)


def buildMinHeightBst(array, start, end):    
    if start > end:
        return
    mid = (start + end) // 2
    bst =  BST(array[mid])
    bst.left = buildMinHeightBst(array, start, mid -1)
    bst.right = buildMinHeightBst(array, mid + 1, end)
    return bst



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minHeightBst(array)
