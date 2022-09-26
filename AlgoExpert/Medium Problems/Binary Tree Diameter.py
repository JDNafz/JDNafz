'''
Calculate longest path


🔵 Medium
https://www.algoexpert.io/questions/binary-tree-diameter
'''
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    global longestPath
    longestPath = 0
    binaryTreeDiameterHelper(tree)
    return longestPath

def binaryTreeDiameterHelper(tree):
    global longestPath
    if tree is None:
        return 0
    
    left = binaryTreeDiameterHelper(tree.left)
    right = binaryTreeDiameterHelper(tree.right)

    current_longestPath = left + right
    longestPath = max(current_longestPath, longestPath)
    return max(left,right) + 1
