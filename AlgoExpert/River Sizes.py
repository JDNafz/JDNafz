def riverSizes(matrix):
    global currRiver 
    currRiver = 0
    results = []
    for row in range(len(matrix)):
        # print("row#{}, rowVal:{}, \n{}\n".format(row,matrix[row],results))
        for col in range(len(matrix[0])):
            current_location = matrix[row][col]
            if matrix[row][col] == 1:
                currRiver = 1
                matrix[row][col] = -1
                findRiver(row,col,matrix,results,currRiver)
    print(results)
    sum = 0
    for i in results:
        sum+=i
    print(sum)
    return results

def findRiver(row,col,matrix,results,currRiver):
    if checkRight(row,col,matrix,results,currRiver):
        findRiver(row,col,matrix,results,currRiver)
    elif checkDown(row,col,matrix,results,currRiver):
        findRiver(row,col,matrix,results,currRiver)
    elif checkLeft(row,col,matrix,results,currRiver):
        findRiver(row,col,matrix,results,currRiver)
    elif checkUp(row,col,matrix,results,currRiver):
        findRiver(row,col,matrix,results,currRiver)
    else:
        results.append(currRiver)

    for i in range(len(matrix)):
        print(matrix[i])
    print(results)
    print("\n")
    return

def checkRight(row,col,matrix,results,currRiver):
    if col < len(matrix[row]) - 1:
        if checkit(row,col+1,matrix,currRiver):
            return True
    return False

def checkLeft(row,col,matrix,results,currRiver):
    if col != 0:
        if checkit(row,col-1,matrix,currRiver):
            return True
    return False

def checkDown(row,col,matrix,results,currRiver):
    if row < len(matrix)-1:
        if checkit(row+1,col,matrix,currRiver):
            return True
    return False

def checkUp(row,col,matrix,results,currRiver):
    if row != 0:
        if checkit(row-1,col,matrix,currRiver):
            return True
    return False


def checkit(row,col,matrix,currRiver):
    if matrix[row][col] == 1:
        matrix[row][col] = -1
        currRiver += 1
        print(currRiver)
        return True
    return False

# riverSizes([
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0]
# ])

riverSizes([
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0]
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