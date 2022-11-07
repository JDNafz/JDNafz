'''

🔴 Hard
https://www.algoexpert.io/questions/merge-linked-lists
'''


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p2 = headTwo
    holder = None
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            holder = p1
            p1 = p1.next
        else:
            if holder is not None:
                holder.next = p2 
            holder = p2
            p2 = p2.next
            holder.next = p1
    if p1 is None:
        holder.next = p2      
        
    printList(headOne)
    printList(headTwo)
    return headOne if headOne.value < headTwo.value else headTwo



def printList(p1):
    array = []
    while p1 is not None:
        array.append(p1.value)
        p1 = p1.next
    print(array)

# headOne = LinkedList(2)
# p1 = headOne
# for num in [6,7,8]:
#     p1.next = LinkedList(num)
#     p1 = p1.next

# headTwo = LinkedList(1)
# p1 = headTwo
# for num in [3,4,5,9,10]:
#     p1.next = LinkedList(num)
#     p1 = p1.next

headOne = LinkedList(2)
p1 = headOne
for num in [6,7,8]:
    p1.next = LinkedList(num)
    p1 = p1.next

headTwo = LinkedList(1)
p1 = headTwo
for num in [3,4,5,9,10]:
    p1.next = LinkedList(num)
    p1 = p1.next

mergeLinkedLists(headOne, headTwo)