'''
Flip the tree lef/right 

🔵 Medium
https://www.algoexpert.io/questions/invert-binary-tree

'''

def invertBinaryTree(tree):
    if tree is None:
        return 
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    tree.left,tree.right = tree.right,tree.left
    return 


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

