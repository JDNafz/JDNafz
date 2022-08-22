'''
add tree nodes to an array traversing down the left side.
It is basically asking to see the pattern of recursion on a given
tree with letters as nodes and as many children as desired.
🟢 Easy Difficulty

https://www.algoexpert.io/questions/depth-first-search
'''
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.



    
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
