'''


🔵 Medium Difficulty

https://www.algoexpert.io/questions/validate-bst

'''


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree,minVal,maxVal):
    if tree == None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False
    leftTest = validateBSTHelper(tree.left, minVal, tree.value)
    return leftTest and validateBSTHelper(tree.right, tree.value,maxVal)