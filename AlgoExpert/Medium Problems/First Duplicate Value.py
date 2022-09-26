'''
Find the first duplicate value in an array. Given array 
will be integers between 1 and n

🔵 Medium Difficulty
https://www.algoexpert.io/questions/first-duplicate-value
'''


# This method runs in constant time, mutating the orginal 
# array to be negative at the INDEX of the VALUE
# if array[0] == 10
#    array[10] *= -1
#Turns it negative it shows that Value has already been accessed.
def firstDuplicateValue(array):
    # Write your code here.
    for i in array:
        absValue = abs(i)
        if array[absValue-1] < 0:
            print(absValue)
            return absValue
        array[absValue -1] *= -1
    print("-1")
    return -1

firstDuplicateValue([2, 1, 5, 2, 3, 3, 4])



# O(n) Time | O(n) Space
# def firstDuplicateValue(array):
#     # Write your code here.
#     numbers = {}
#     for i in array:
#         if i in numbers:
#             return i
#         else:
#             numbers[i] = 1
#     return -1


# Brute force method
# # O(n^2) time \ O(1) Space
# def firstDuplicateValue(array):
#     minIndex = len(array)
#     for i in range(len(array)):
        
#         for j in range(i+1,len(array)):
#             if array[i] == array [j]:
#                 minIndex = min(j, minIndex)
#     if minIndex == len(array):
#         return -1
#     return array[minIndex]