'''
🔵 Medium
https://www.algoexpert.io/questions/remove-kth-node-from-end
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    left, right = head, head
    print("k:",k)
    for _ in range(k):
        right = right.next

    #if k was longer than string remove the head
    if right is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while right.next is not None:
        left = left.next
        right = right.next
    left.next = left.next.next