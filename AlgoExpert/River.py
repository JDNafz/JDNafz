def riverSizes(matrix):
    global currRiver 
    currRiver = 0
    results = []
    riverCounter = -1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            current_location = matrix[row][col]
            if matrix[row][col] == 1:
                currRiver = 1
                results.append(currRiver)
                riverCounter += 1
                matrix[row][col] = -1
                findRiver(row,col,matrix,results)
                addRiver(currRiver,results,riverCounter)
            
    print(results)
    # checkSum(results)    
    return results

def findRiver(row,col,matrix,results):
    global currRiver
    if checkRight(row,col,matrix,results):
        findRiver(row,col+1,matrix,results)
    if checkDown(row,col,matrix,results):
        findRiver(row+1,col,matrix,results)
    if checkLeft(row,col,matrix,results):
        findRiver(row,col-1,matrix,results)
    if checkUp(row,col,matrix,results):
        findRiver(row-1,col,matrix,results)
    #print to check work:
    # printStep(matrix,results)
    return

def checkRight(row,col,matrix,results):
    if col < len(matrix[row]) - 1:
        if checkit(row,col+1,matrix):
            return True
    return False

def checkLeft(row,col,matrix,results):
    if col != 0:
        if checkit(row,col-1,matrix):
            return True
    return False

def checkDown(row,col,matrix,results):
    if row < len(matrix)-1:
        if checkit(row+1,col,matrix):
            return True
    return False

def checkUp(row,col,matrix,results):
    if row != 0:
        if checkit(row-1,col,matrix):
            return True
    return False


def checkit(row,col,matrix):
    global currRiver
    if matrix[row][col] == 1:
        matrix[row][col] = -2
        currRiver += 1
        return True
    else:
        return False

def checkSum(results):
    sum = 0
    for i in results:
        sum+=i
    print(sum)

def printStep(matrix,results):
    for i in range(len(matrix)):
        print(matrix[i])
    print(results)
    print("\n")

def addRiver(currRiver,results,riverCounter):
    results[riverCounter] = currRiver
    currRiver = 0
# riverSizes([
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0]
# ])

# riverSizes([
#   [1, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0],
#   [0, 1, 0, 1, 0],
#   [1, 0, 0, 1, 1],
#   [1, 1, 1, 0, 0]
# ])
# [1, 2, 3, 4]

# riverSizes([
#     [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
#     [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
#     [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
#   ])