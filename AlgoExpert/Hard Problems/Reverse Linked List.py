'''
Reverse the linked list in O(n) time O(1) space
🔴 Hard
https://www.algoexpert.io/questions/reverse-linked-list
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    hold = head
    while head.next is not None: 
        moving = head.next
        head.next = head.next.next
        moving.next = hold 
        hold = moving
    head = hold
    return head