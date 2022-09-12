'''
Find the k-th largest value.

🔵 Medium
https://www.algoexpert.io/questions/find-kth-largest-value-in-bst

'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
# def findKthLargestValueInBst(tree, k):
#     array = maxOrderTraverse(tree,k, [])
#     return array[k-1]

# def maxOrderTraverse(tree, k, array):
#     if len(array) == k:
#         print("done",array[k-1])
#         return array[k-1]
#     if tree is not None:  
#         maxOrderTraverse(tree.right,k, array)
#         array.append(tree.value)
#         maxOrderTraverse(tree.left,k , array)
#     print(array)
#     return array
    

# O(h + k) time | O(h) space where h is the height and k is the input parameter 
class kInfo:
    def __init__(self,k,kValue):
        self.k = k
        self.kValue = kValue

def findKthLargestValueInBst(tree, k):
    kinfo = kInfo(0,-1)
    maxOrderTraverse(tree,k, kinfo)
    return kinfo.kValue

def maxOrderTraverse(tree, k, kinfo):
    if tree is None or kinfo.k >= k:
        return
    maxOrderTraverse(tree.right,k, kinfo)
    if kinfo.k < k:
        kinfo.k += 1
        kinfo.kValue = tree.value
    maxOrderTraverse(tree.left,k, kinfo)
    