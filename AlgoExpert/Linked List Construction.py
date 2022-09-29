



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
        if node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            node.next = self.head
            self.head = node
        node.prev = None
        

    def setTail(self, node):
        if node == self.head:
            self.head = node.next
            node.next.prev = None
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        node.next = None
            

    def insertBefore(self, node, nodeToInsert):
        if node == self.head:
            self.head = nodeToInsert
        else:
            nodeToInsert.prev = node.prev
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        nodeToInsert.next = node



    def insertAfter(self, node, nodeToInsert):
        if node == self.tail:
            self.tail = nodeToInsert
        else:
            nodeToInsert.next = node.next 
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        nodeToInsert.prev = node

    def insertAtPosition(self, position, nodeToInsert):
        if self.head == None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return
        node = self.head
        for _ in range(1,position,1):
            node = node.next
        self.insertBefore(node, nodeToInsert)
            

    def removeNodesWithValue(self, value):
        self.nodeToRemove = []
        if self.containsNodeWithValue(value):
            for node in self.nodeToRemove:
                self.remove(node)

        
    def remove(self, node):
        if node == self.head:
            self.head = node.next
            node.next.prev = None
            return
        if node == self.tail:
            self.tail = node.prev
            node.prev.next = None
            return
        if node != self.head and node != self.tail:
            node.prev.next, node.next.prev = node.next, node.prev
        
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.nodeToRemove.append(node)
            node = node.next
        if self.nodeToRemove != []:
            return True 
        return False

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