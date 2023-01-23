'''
Sort the stack using recursion and only using .pop() .append() and peek (stack[-1])
🔵 Medium Difficulty

https://www.algoexpert.io/questions/sort-stack
'''

def sortStack(stack):
    if len(stack) == 0:
        # print("on our way back!")
        return stack
    popped = stack.pop()

    sortStack(stack)
    
    sortIt(stack,popped)
    
    print(stack)
    return stack

def sortIt(stack, value):
    if len(stack) == 0 or stack[len(stack) -1] <= value:
        stack.append(value)
        return
    outOfOrder = stack.pop()
    sortIt(stack, value)
    stack.append(outOfOrder)


s0 = [3,2,1]
s01 = [-5,1,6,-7,0,-3,8,9]
sortStack(s01)


