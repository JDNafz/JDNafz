class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    difference = abs(heightCheck(tree.left,0) - heightCheck(tree.right,0))
    if difference == 1 or difference == 0:
        return True
    return False

def heightCheck(node,height):
    if node is None:
        return
    heightCheck(node.left)
    heightCheck(node.right)

