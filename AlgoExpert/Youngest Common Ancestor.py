# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d1 = findDepth(topAncestor,descendantOne)
    d2 = findDepth(topAncestor,descendantTwo)
    # print("Depth of {}:{}".format(descendantOne.name,d1),"Depth of {}:{}".format(descendantTwo.name,d2))
    if d1 > d2:
        smaller = descendantTwo
        larger = descendantOne
    else:
        smaller = descendantOne
        larger = descendantTwo
    dif = abs(d1-d2)

    for _ in range(dif):
        larger = larger.ancestor
    while smaller != larger:
        smaller = smaller.ancestor
        larger = larger.ancestor
    if smaller is None:
        return topAncestor
    return smaller

def findDepth(root,node):
    depth = 0
    while node != root:
        node = node.ancestor
        depth += 1
    return depth


# A = AncestralTree("A")
# B = AncestralTree("B")
# B.ancestor = A

# C = AncestralTree("C")
# D = AncestralTree("D")
# E = AncestralTree("E")
# F = AncestralTree("F")
# G = AncestralTree("G")
# H = AncestralTree("H")
# I = AncestralTree("I")
# H.ancestor = D
# I.ancestor = D
# D.ancestor = B
# E.ancestor = B
# F.ancestor = C
# G.ancestor = C
# C.ancestor = A

# getYoungestCommonAncestor(A,E,I)
# getYoungestCommonAncestor(A,B,A)