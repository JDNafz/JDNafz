# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):        
        #THIS IS MY CODE:
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)     
        print(array)
        return array

# A = Node("A")
# A.addChild("B")
# A.addChild("C")
# A.addChild("D")
# B = A.children[0]
# D = A.children[2]
# B.addChild("E")
# B.addChild("F")
# F = B.children[1]
# F.addChild("I")
# F.addChild("J")
# D.addChild("G")
# G = D.children[0]
# G.addChild("K")




array = []
A.breadthFirstSearch(array)
