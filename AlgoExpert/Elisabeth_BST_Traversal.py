# Sorry I don't know how this works and am just guessing
class BinaryTreeNode:
  def __init__(self, data):
    self.value = data
    self.left = None
    self.right = None
     
def insert(root,newValue):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.value:
        root.left=insert(root.left,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.right=insert(root.right,newValue)
    return root

def inOrderTraverse(tree, array):
    if tree is None:
        return array
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    

def preOrderTraverse(tree, array):
    if tree is None:
        return array
    print(array)
    array.append(tree.value)
    array = preOrderTraverse(tree.left, array)
    array = preOrderTraverse(tree.right, array)

def postOrderTraverse(tree, array):
    if tree is None:
        return array
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)

root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
print("Printing values of binary tree in preorder Traversal.")
print(preOrderTraverse(root,[]))

