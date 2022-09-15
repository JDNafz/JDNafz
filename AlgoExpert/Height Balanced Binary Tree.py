class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class InfoTracker:
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    result = balancedHelper(tree)
    return result.isBalanced

def balancedHelper(node):
    if node is None:
        return InfoTracker(True, -1)
    
    left = balancedHelper(node.left)
    right = balancedHelper(node.right)

    isBalanced = (  left.isBalanced and right.isBalanced and abs(left.height - right.height) <=1    )

    height = max(left.height,right.height) + 1
    return InfoTracker(isBalanced, height)