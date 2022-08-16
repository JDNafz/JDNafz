'''
Branch Sums asks you to sum the values in each Binary Tree branch. 
Basically from every leaf of the Binary Tree summ all of its parents values.

🟢 Easy Difficulty


https://www.algoexpert.io/questions/branch-sums

'''




# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# branchSums is a function that returns a list
def branchSums(root):
    node = root
    totals = []
    if node.left is None and node.right is None:
        #if it's a leaf, return node.value
        return [node.value]
    elif node.left is not None and node.right is not None:
        # if it has two kids
        totals = []
        for element in branchSums(node.left):
            totals.append( element + node.value)
        for element in branchSums(node.right):
            totals.append(element + node.value)
        return totals
    
    elif node.left is not None:
        print(r"""  """)
        totals = []
        for element in branchSums(node.left):
            totals.append(element + node.value)
        return totals
    elif node.right is not None:
        totals = []
        for element in branchSums(node.right):
            totals.append(element + node.value)
        return totals
    return totals
 