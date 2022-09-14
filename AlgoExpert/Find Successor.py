'''
Find the next item following a specific node in a BT assuming it is being sorted using inOrder Traversal
🔵 Medium
https://www.algoexpert.io/questions/find-successor
'''
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    if node.right is not None:
        return leftMostChild(node.right)
    return rightMostParent(node)

    
def leftMostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def rightMostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent