# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    if tree.left is not None and tree.right is None:
        if tree.left.value >= tree.value:
            
            return False
        else:
            return validateBst(tree.left)
    elif tree.right is not None and tree.left is None:
        if tree.right.value < tree.value:
            return False
        else:
            return validateBst(tree.right)
    return True


    '''
                 10
              /      \
            5         15
          /  \          \
         2    5-2        22
        /       \            
       1        11         
    
    
    
    
    
    
    '''