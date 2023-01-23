'''
Look through two linked lists if they contain the same number, all other numbers following it will also match until the end.
find the first matching number and return it or return None.

🔵 Medium Difficulty
https://www.algoexpert.io/questions/merging-linked-lists
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    one = linkedListOne
    two = linkedListTwo
    countOne = 0
    countTwo = 0

    #check length of each list
    while one:
        countOne += 1
        one = one.next
    while two:
        countTwo += 1
        two = two.next
    
    #adjust the starting position if one of the lists is longer
    while countOne > countTwo:
        countOne -= 1
        linkedListOne = linkedListOne.next
    while countTwo > countOne:
        countTwo -= 1
        linkedListTwo = linkedListTwo.next

    #check for a match
    while linkedListOne:
        if linkedListOne == linkedListTwo:
            return linkedListOne
        else:
            linkedListOne = linkedListOne.next
            linkedListTwo = linkedListTwo.next
    
    return None