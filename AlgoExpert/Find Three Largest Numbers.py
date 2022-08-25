'''
Find largest three numbers return from least to greatest in a list.
🟢 Easy Difficulty
https://www.algoexpert.io/questions/find-three-largest-numbers
'''
def findThreeLargestNumbers(array):
    # Write your code here.
    a,b,c = float('-inf'),float('-inf'),float('-inf')
    for element in array:
        print([a,b,c])
        if element >= c:
            a = b
            b = c
            c = element
        elif element >= b:
            a = b
            b = element
        elif element >= a:
            a = element
    return [a,b,c]