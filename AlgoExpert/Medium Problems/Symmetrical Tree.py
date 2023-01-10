'''
return True of False if the binary tree is symmetrical

🔵 Medium
https://www.algoexpert.io/questions/symmetrical-tree

'''
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def symmetricalTree(tree):
    return symmetricalTrees(tree.left, tree.right)


def symmetricalTrees(left , right):
    if left is not None and right is not None and left.value == right.value:
        return symmetricalTrees(left.left, right.right) and symmetricalTrees(left.right, right.left)

    return left == right