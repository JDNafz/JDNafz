'''
Write three functions to output an array that has the BST nodes sorted "in order" "


🔵 Medium
https://www.algoexpert.io/questions/bst-traversal
'''
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array
    
    
def postOrderTraverse(tree, array):
    if tree.left is not None:
        inOrderTraverse(tree.left, array)
    if tree.right is not None:
        inOrderTraverse(tree.right,array)
    array.append(tree.value)
    return array

def preOrderTraverse(tree, array):
    array.append(tree.value)
    if tree.left is not None:
        inOrderTraverse(tree.left, array)
    if tree.right is not None:
        inOrderTraverse(tree.right,array)
    return array

