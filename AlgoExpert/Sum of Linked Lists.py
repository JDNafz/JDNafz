'''
🔵 Medium
https://www.algoexpert.io/questions/sum-of-linked-lists
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    One, Two, carry = linkedListOne, linkedListTwo, 0
    temp = One.value + Two.value
    if temp >= 10:
        temp = temp % 10
        carry = 1
    FinalList = LinkedList(temp)
    Final = FinalList
    One, Two = One.next, Two.next
    while One is not None or Two is not None:
        if One is None:
            temp1 = 0
        else:
            temp1 = One.value
        if Two is None:
            temp2 = 0
        else:
            temp2 = Two.value
        
        temp = temp1 + temp2 + carry
        carry = 0
        if temp >= 10:
            temp = temp % 10
            carry = 1
        Final.next = LinkedList(temp)

        if One is not None:
            One = One.next
        if Two is not None:
            Two = Two.next
        Final = Final.next
    if carry:
        Final.next = LinkedList(1)
        carry = 0

    return FinalList