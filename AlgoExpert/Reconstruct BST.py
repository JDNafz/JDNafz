'''
construct a BST from an array given that the array was 
constructed by pre-order traversal

🔵 Medium
https://www.algoexpert.io/questions/reconstruct-bst


'''
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ROOT:
    def __init__(self,idx):
        self.idx = idx

def reconstructBst(preOrderTraversalValues):
    root = ROOT(0)
    return reconstructBSTHelper(preOrderTraversalValues, root, float('-inf'), float('inf'))

def reconstructBSTHelper(array, currentRoot,lower,upper):
    if currentRoot.idx == len(array):
        return None
    rootValue = array[currentRoot.idx]
    if rootValue < lower or rootValue >= upper:
        return None
    currentRoot.idx += 1
    left = reconstructBSTHelper(array, currentRoot, lower, rootValue)
    right = reconstructBSTHelper(array, currentRoot, rootValue, upper)
    
    print (BST(rootValue,left,right))
    return BST(rootValue,left,right)

array = [10, 4, 2, 1, 5, 17, 19, 18]
reconstructBst(array)