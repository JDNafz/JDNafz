# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # return helperFindKthLargestValueInBst(tree, k, [])
    return maxOrderTraverse(tree,k, [])

def maxOrderTraverse(tree, k, array):
    if tree is not None:  
        maxOrderTraverse(tree.right,k, array)
        array.append(tree.value)
        maxOrderTraverse(tree.left,k , array)
    print(array)
    if len(array) == k:
        print(array[k-1])
        return array[k-1]



        # This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # return helperFindKthLargestValueInBst(tree, k, [])
    array = maxOrderTraverse(tree,k, [])
    return array[k-1]

def maxOrderTraverse(tree, k, array):
    if len(array) == k:
        print("done",array[k-1])
        return array[k-1]
    if tree is not None:  
        maxOrderTraverse(tree.right,k, array)
        array.append(tree.value)
        maxOrderTraverse(tree.left,k , array)
    print(array)
    return array
    
