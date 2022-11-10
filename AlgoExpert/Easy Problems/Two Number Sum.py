'''
🟢 Easy Difficulty
https://www.algoexpert.io/questions/two-number-sum
'''

# O(n) time | O(n) Space
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == targetSum and array[i] != array[j]:
                return [array[i], array[j]]
    return []



# O(n^2) time | O(1) Space
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i] + array[j] == targetSum and array[i] != array[j]:
#                 return [array[i], array[j]]
#     return []
