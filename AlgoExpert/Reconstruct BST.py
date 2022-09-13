 # This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class info:
    def __init__(self,root,current):
        self.root = root
        self.current = current

def reconstructBst(preOrderTraversalValues):
    info.root = preOrderTraversalValues
    tree = BST(preOrderTraversalValues[0],0)
    return reconstructBstHelper(preOrderTraversalValues,tree,info)
    
def reconstructBstHelper(preOrderTraversalValues,tree,info):
    if preOrderTraversalValues[info.current] < preOrderTraversalValues[info.current]:
        tree.left = preOrderTraversalValues[info.current]
        info.current += 1
        reconstructBstHelper(preOrderTraversalValues,tree.left,info)
    else:
        preOrderTraversalValues[info.current] < preOrderTraversalValues[info.root]:
        tree.right = preOrderTraversalValues[info.current]





array = [10, 4, 2, 1, 5, 17, 19, 18]
reconstructBst(array)