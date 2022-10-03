# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    
    if head < 0:
        head.value = abs(head.value)
        
        return head
    head.value = 
        # if val is below zero return node
