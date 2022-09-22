
def removeIslands(matrix):
    visited = [[False for _ in row] for row in matrix]
    
    for row in range(len(matrix)):
        col = len(matrix[0])
        if visited[row][col]:
            continue    
        initialSearch(row,col,matrix,visited)
    for row in range(len(matrix)):
        col = 0
        if visited[row][col]:
            continue  
        initialSearch(row,col,matrix,visited)
    for col in range(len(matrix[0])):
        row = 0
        if visited[row][col]:
            continue 
        initialSearch(row,col,matrix,visited)
    for col in range(len(matrix[0])):        
        row = len(matrix)
        col = 0
        if visited[row][col]:
            continue 
        initialSearch(row,col,matrix,visited)    

    printMatrix(matrix)
    return matrix

def initialSearch(row,col,matrix,visited):
    nodesToCheck = []
    while len(nodesToCheck) > 0:
        currentNode = nodesToCheck.pop()
        row,col = currentNode[0],currentNode[1]
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        matrix[row][col] = 2
        unvisitedNeighbors = getUnvisitedNeighbors(row,col,matrix,visited)
        for pair in unvisitedNeighbors:
            nodesToCheck.append(pair)

def getUnvisitedNeighbors(row,col,matrix,visited):
    pairs = []
    #up
    if row > 0 and not visited[ row - 1][col]:
        pairs.append([row - 1,col])
    #down
    if row < len(matrix)-1 and not visited[row + 1][col]:
        pairs.append([row + 1,col])
    #left
    if col > 0 and not visited[row][col-1]:
        pairs.append([row ,col-1])
    if col < len(matrix[0])-1 and not visited[row][col+1]:
        pairs.append([row,col+1])
    return pairs





def printMatrix(matrix):
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