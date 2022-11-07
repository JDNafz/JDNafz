'''

🔵 Medium
https://www.algoexpert.io/questions/search-in-sorted-matrix
'''
#O(n+m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


#near O(n*m)Time | O(1) Space
# def searchInSortedMatrix(matrix, target):
#     for i in reversed(range(len(matrix))):
#         if target < matrix[i][0]:
#             continue
#         for j in range(len(matrix[i])):
#             if target == matrix[i][j]:
#                 return [i, j]
#             elif target > matrix[i][j]:
#                 continue
#             else:
#                 break
#     return [-1, -1]