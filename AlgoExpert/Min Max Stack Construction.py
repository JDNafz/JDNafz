'''🔵'''

class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        minMaxDict = {"min": number, "max": number}
        if len(self.minMaxStack):
            currentStack = self.minMaxStack[len(self.minMaxStack)-1]
            minMaxDict["min"] = min(currentStack["min"], number)
            minMaxDict["max"] = max(currentStack["max"], number)
        self.minMaxStack.append(minMaxDict)
        self.stack.append(number)


    def getMin(self):
        if len(self.minMaxStack):
            # print(self.minMaxStack[-1])
            return self.minMaxStack[-1]["min"]

    def getMax(self):
        if len(self.minMaxStack):
            # print(self.maxStack[-1])
            return self.minMaxStack[-1]["max"]

# peppar = MinMaxStack()
# peppar.push(5)
# peppar.getMin()




import unittest
def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)
