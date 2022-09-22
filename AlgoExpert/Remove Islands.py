
def removeIslands(matrix):
    visited = [[False for _ in row] for row in matrix]
    
    for row in range(len(matrix)):
        col = len(matrix[0])
        initialSearch(row,col,matrix,2)
        col = 0
        initialSearch(row,col,matrix,2)
    for col in range(len(matrix[0])):
        row = 0
        initialSearch(row,col,matrix,2)
        row = len(matrix)
        initialSearch(row,col,matrix,2)    
    return matrix

def initialSearch(row,col,matrix,change):
    pass


def printStep(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")

removeIslands([
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
])


# removeIslands([
#     [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
#     [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
#     [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
#   ])