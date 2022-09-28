# This is an input class. Do not edit.
from os import link


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
        else:
            headNode = self.head
            headNode.prev = node
            node.next = headNode
            self.head = node

    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            tailNode = self.tail
            tailNode.next = node
            node.prev = tailNode
            self.tail = node
            

    def insertBefore(self, node, nodeToInsert):
        if node == self.head:
            self.head = nodeToInsert
        else:
            nodeToInsert.prev = node.prev
        node.prev.next, nodeToInsert.next, node.prev = nodeToInsert, node, nodeToInsert



    def insertAfter(self, node, nodeToInsert):
        if node == self.tail:
            self.tail = nodeToInsert
        else:
            nodeToInsert.next = node.next 
        node.next.prev, nodeToInsert.prev, node.next = nodeToInsert, node, nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        node = self.head
        for _ in range(1,position,1):
            node = node.next
        # print("insertBefore({}, {})".format(node.value,nodeToInsert.value))
        self.insertBefore(node, nodeToInsert)
            

    def removeNodesWithValue(self, value):
        node = self.containsNodeWithValue(value) 
        while node is not None:
            self.remove(node)
            node = self.containsNodeWithValue(value)

        
    def remove(self, node):
        print("remove({})".format(node.value))
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
                print("yes contains {}".format(value))
                return node 
            node = node.next
        return None

    def printHead2Tail(self):
        values = []
        nodeNames = []
        node = linkedList.head
        while node is not None:
            values.append(node.value)
            nodeNames.append(node)
            node = node.next
        print(values)
        return nodeNames

def printPointers(array):
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


linkedList.setHead(four)
linkedList.setTail(six)
linkedList.insertBefore(six,three)

head2Tail = linkedList.printHead2Tail()

linkedList.insertAfter(six,three2)
linkedList.insertAtPosition(1,three3)
linkedList.remove(two)
linkedList.containsNodeWithValue(5)




# printPointers(head2Tail)
# print("Head/Tail",linkedList.head.value, linkedList.tail.value )

head2Tail = linkedList.printHead2Tail()