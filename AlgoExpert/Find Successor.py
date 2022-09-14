
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    global complete 
    complete = False
    return inOrderTraverse(tree,node)


def inOrderTraverse(tree, node):
    global complete
    if complete == True or tree is None:
        return
    if tree.left is not None:
        inOrderTraverse(tree.left,node)
    # CURR TREE array.append(tree.value)
    if tree.right is not None:
        inOrderTraverse(tree.right,node)
    
    if tree.value == node
    return array