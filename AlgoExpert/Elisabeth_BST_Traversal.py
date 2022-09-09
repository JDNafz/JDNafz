# Sorry I don't know how this works and am just guessing
def inOrderTraverse(tree, array):
    if tree is None:
        return array
    inOrderTraverse(tree.left)
    array.append(tree.value)
    inOrderTraverse(tree.right)
    

def preOrderTraverse(tree, array):
    if tree is None:
        return array
    array.append(tree.value)
    preOrderTraverse(tree.left)
    preOrderTraverse(tree.right)

def postOrderTraverse(tree, array):
    if tree is None:
        return array
    postOrderTraverse(tree.left)
    postOrderTraverse(tree.right)
    array.append(tree.value)


