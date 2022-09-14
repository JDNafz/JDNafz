
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    if node.left is not None:
        return leftMostChild(node.left)

def leftMostChild(tree):
    if tree.left is None:
        return
    leftMostChild(tree.left)
    print(tree.value)
    return tree




# node1 = BinaryTree(1,2,3,None)
# node2 = BinaryTree(2,4,5,1)
# node4 = BinaryTree(4,8,9,2)
# node8 = BinaryTree(8,None,None,4)
# node9 = BinaryTree(9,None,None,4)
# node5 = BinaryTree(5,None,None,2)
# node3 = BinaryTree(3,6,7,1)
# node6 = BinaryTree(6,None,None,3)
# node7 = BinaryTree(7,None,None,3)

