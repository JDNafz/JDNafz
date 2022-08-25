'''
Fibonacci - for this problem assume 
getNthFib(1) = F0 = 0
getNthFib(2) = F1 = 1


https://www.algoexpert.io/questions/nth-fibonacci

'''


def getNthFib(n):
    # Write your code here.
    
    penUlt = 0
    ult = 1
    current = 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(n-2):
        current = penUlt + ult
        penUlt,ult = ult, current
    return current