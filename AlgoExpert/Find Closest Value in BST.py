'''
Find closest value. You may assume there will only be one closest value.
🟢 Easy Difficulty

https://www.algoexpert.io/questions/find-closest-value-in-bst
'''
def findClosestValueInBst(tree, target):
    # Write your code here.
    
    closestTree = tree.value
    closestDif = abs(tree.value - target)
    while tree is not None:  
        if abs(tree.value - target) < closestDif:
            closestTree = tree.value
            closestDif = abs(tree.value - target)
        if target < tree.value:
            tree = tree.left
        else: 
            tree = tree.right

    return closestTree 

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
