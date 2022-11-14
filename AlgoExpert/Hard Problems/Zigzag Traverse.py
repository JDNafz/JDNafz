'''
start upper left proceede diagonally (down/left and up/right) \
until arriving at bottom right corner. At edges wrap to next row.
🔴 Hard
https://www.algoexpert.io/questions/zigzag-traverse
'''
def zigzagTraverse(array):
    n = m = 0
    traversal = []
    Up = 1
    Over = 1

    while len(traversal) < (len(array) * len(array[0])):
        if len(traversal) == 0:
            traversal.append(array[n][m])
            if len(array) * len(array[0]) == 1:
                return traversal

        if Up == 1:
            Over = -1
        if inB(n + Up, m + Over, array):  # if diagonal
            n += Up
            m += Over
            traversal.append(array[n][m])
        else:
            if Up == -1:                   #if UpDiag
                Up = 1
                Over = -1
                if inB(n, m + 1, array):            #right
                    m += 1
                    traversal.append(array[n][m])
                else:                                  #down
                    if inB(n + 1, m, array):
                        n += 1
                        traversal.append(array[n][m])

            else:                          #if DownDiag
                Up = -1
                Over = 1
                if inB(n + 1, m, array):               #down
                    n += 1
                    traversal.append(array[n][m])   
                else:
                    if inB(n, m + 1, array):           #right
                        m += 1
                        traversal.append(array[n][m])                
    print(traversal)
    return traversal

def inB(n, m, array):
    #inBounds
    if 0 <= n <= len(array) - 1 and 0 <= m <= len(array[0]) - 1:
        return True
    return False




# #Answer:
# # [1, 2, 3, ... , 16]
# test1 = [
#   [1, 3, 4, 10],
#   [2, 5, 9, 11],
#   [6, 8, 12, 15],
#   [7, 13, 14, 16]
# ]
# zigzagTraverse(test1)

# test2 = [
#     [1, 2, 3, 4, 5]
#   ]
# # zigzagTraverse(test2)