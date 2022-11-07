'''

🔵 Medium
https://www.algoexpert.io/questions/linked-list-construction
'''

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail,node)

    
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1 
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def pHeadToTail(self):
        values = []
        nodeNames = []
        node = self.head
        while node is not None:
            values.append(node.value)
            nodeNames.append(node)
            node = node.next
        print("H:", values)
        return nodeNames

    def pTailToHead(self):
        values = []
        nodeNames = []
        node = self.tail
        while node is not None:
            values.append(node.value)
            nodeNames.append(node)
            node = node.prev
        values2 = []
        for i in reversed(values):
            values2.append(i)

        print("T:", values2)
        return nodeNames

    def pPointers(self,array):
        for node in array:
            if node.prev is not None:
                prevvar = node.prev.value
            else:
                prevvar = "N"
            if node.next is not None:
                nextvar = node.next.value
            else:
                nextvar = "N"
            print("    {} \n  /   \ \n {}     {}".format(node.value, prevvar, nextvar))
    def pBoth(self):
        self.pHeadToTail()
        self.pTailToHead()

def t1():
    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    linkedList.setHead(five)
    linkedList.setHead(four)
    linkedList.setHead(three)
    linkedList.setHead(two)
    linkedList.setHead(one)

    linkedList.pBoth()
    linkedList.setHead(four)
    print(linkedList.head.value)
    linkedList.pBoth()
    
    linkedList.setTail(six)

    
    linkedList.insertBefore(six,three)
    linkedList.insertAfter(six,three2)

    linkedList.pBoth()


    linkedList.insertAtPosition(1,three3)
    linkedList.removeNodesWithValue(3)
    linkedList.remove(two)
    linkedList.containsNodeWithValue(5)



def t2():
    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)

    linkedList.setHead(one)
    linkedList.pHeadToTail()
    linkedList.insertBefore(one, two)
    linkedList.pHeadToTail()
# t1()