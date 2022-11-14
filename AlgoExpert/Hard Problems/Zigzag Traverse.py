def zigzagTraverse(array):
    # array [row] [col]
    # array  [n]   [m]
    
    n = m = 0
    traversal = []
    goN = goM = 1
    if len(array) < 0 and len(array[0]) < 0:
        traversal.append(array[n][m])
        n + 1
        while len(traversal) <= (len(array) * len(array[0])):
            pass


    print(traversal)
    return traversal



# def right(n,m):
#     m += 1
#     return m

#Answer:
# [1, 2, 3, ... , 16]
test1 = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]
zigzagTraverse(test1)