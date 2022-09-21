def riverSizes(matrix):
    results = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                currRiver = 0
                findRiver(row,col,matrix,results,currRiver)
    print(results)
    return results

def findRiver(row,col,matrix,results,currRiver):
    matrix[row][col] = -1
    currRiver +=1
    if checkRight(row,col,matrix):
        if matrix[row][col+1] == 1:
            findRiver(row,col+1,matrix,results,currRiver)
    if checkLeft(row,col,matrix):
        if matrix[row][col-1] == 1:
            findRiver(row,col-1,matrix,results,currRiver)
    if checkDown(row,col,matrix):
        if matrix[row+1][col] == 1:
            findRiver(row+1,col,matrix,results,currRiver)
    if checkUp(row,col,matrix):
        if matrix[row-1][col] ==1:
            findRiver (row-1,col,matrix,results,currRiver)
    results.append(currRiver)
    return

def checkRight(row,col,matrix):
    if col != matrix[row][-1]:
        return True
    return False
def checkLeft(row,col,matrix):
    if col != matrix[row][0]:
        return True
    return False
def checkDown(row,col,matrix):
    if row != matrix[-1]:
        return True
    return False
def checkUp(row,col,matrix):
    if row != matrix[0]:
        return True
    return False

riverSizes([
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
])



# def searchRiver(row,col,matrix,array,riverLength):
#     riverLength += 1
#     matrix[row][col] = -1

#     if 1 < row < len(matrix[-1]):
#         searchRiver(row+1, col,   matrix,array,riverLength)
#         searchRiver(row-1, col,   matrix,array,riverLength)
#     if 1 < col < len(matrix[1][0]):
#         searchRiver(row,   col+1, matrix,array,riverLength)
#         searchRiver(row,   col-1, matrix,array,riverLength)

#     if col == 1 and : 
#         searchRiver(row,col,matrix,array)
#     return