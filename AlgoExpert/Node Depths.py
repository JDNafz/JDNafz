'''
return the sum of the depths of all branches in the Binary Tree
🟢 Easy Difficulty

https://www.algoexpert.io/questions/node-depths
'''
def nodeDepths(root,depth = -1):
    # Write your code here.
    if root.left is None and root.right is None:
        depth +=1
        print(".   .Node",root.value,"depth:",depth)
        return depth
    if root.left is not None and root.right is not None:
        depth += 1
        print("Node",root.value, "depth,",depth)
        return depth + nodeDepths(root.left,depth) + nodeDepths(root.right,depth)
    elif root.left is not None:
        depth += 1
        return depth + nodeDepths(root.left,depth)
    else:
        depth += 1
        return depth + nodeDepths(root.right,depth)
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
