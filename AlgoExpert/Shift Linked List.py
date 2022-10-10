'''
careful with the edge cases of negative and extremely high numbers!

🔴 Hard
https://www.algoexpert.io/questions/shift-linked-list
'''


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    
    node = head
    listLength = 1
    while node.next is not None:
        node = node.next
        listLength += 1

    offset = abs(k) % listLength
    if offset == 0:
        return head
    if k > 0:
        newtail = listLength - offset
    else:
        newtail = offset

    #set list tail to connect to oldhead
    node.next = head

    #reset node to head
    node = head 
    for _ in range(1, newtail):
        node = node.next
    
    #set the new head
    newhead = node.next
    #set the endpointer to None:
    node.next = None
    
    return newhead