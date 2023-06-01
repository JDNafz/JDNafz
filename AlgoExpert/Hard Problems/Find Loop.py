'''
🔴 Hard 
https://www.algoexpert.io/questions/find-loop
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    node = head
    visited = set()
    while node not in visited:
        visited.add(node)
        node = node.next
    return node

'''# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    node = head
    start = findLoopHelper(node)
    return start


def findLoopHelper(node):
    if node.value < 0:
        node.value = node.value * -1
        print("FOUND", node.value)
        return node
    else:
        # print(head.value)
        node.value = node.value * -1
        node = node.next
        findLoop(node)
    
'''






head = LinkedList(0)
addList = [1,2,3,4,5,6,7,8,9]
node = head
for num in addList:
    if node.next is not None:
        node = node.next
    node.next = LinkedList(num)
    node = node.next
    if num == 4:
        Four = node
node.next = Four

findLoop(head)

# print(node.value, node.next.value)

#Test if I have a loop
# counter = 0
# while counter < 30:
#     print("Node:{} Node.next:{}".format(node.value,node.next.value))
#     counter += 1
#     node = node.next



#print each node once(BEFORE SETTING THE LOOP)
# print(head.value)
# while head.next is not None:
#     head = head.next
#     print(head.value)