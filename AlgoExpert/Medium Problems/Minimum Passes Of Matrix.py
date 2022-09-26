'''
Goal: make all numbers positive in matrix. 
if a negative number is adjacent to a positive number it will flip. 
Calculate how many passes are necessary to flip all the negative numbers.
return -1 if it's impossible.

🔵 Medium
https://www.algoexpert.io/questions/minimum-passes-of-matrix
'''



def minimumPassesOfMatrix(matrix):
    passes = 0
    hasNegative,flip = passThrough(matrix)
    while hasNegative:
        if len(flip) == 0:
            return -1
        else: 
            matrix = flipthem(flip,matrix)
            passes += 1
        hasNegative,flip = passThrough(matrix)

    # printMatrix(matrix)
    # print("PASSES:",passes)
    return passes

def passThrough(matrix):
    flip = []
    neighbors = []
    neighborsBool = False

    #check everything
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                continue

            if matrix[row][col] < 0:
                neighborsBool = True
                neighbors = touching(row,col,matrix)
                for neighbor in neighbors:
                    i,j = neighbor[0],neighbor[1]
                    if matrix[i][j] > 0:
                        flip.append([row,col])
                        break
                    continue

    if neighbors == []:
        if neighborsBool:
            return True,flip
        return False, flip
    return True, flip

def flipthem(flip,matrix):
    printFlipList(flip,matrix)
    for pair in flip:
        row, col = pair[0],pair[1]
        matrix[row][col] *= -1
    print("FLIPPED")
    printMatrix(matrix)
    return matrix

def touching(row,col,matrix):
    neighbors = []
    if col < len(matrix[0]) -1:
        neighbors.append([row,     col + 1])
    if row < len(matrix) - 1:
        neighbors.append([row + 1, col])
    if col > 0:
        neighbors.append([row,     col -1])
    if row > 0:
        neighbors.append([row - 1, col])
    return neighbors

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")

def printFlipList(flip,matrix):
    fliplist = []
    for pair in flip:
        row, col = pair[0],pair[1]
        fliplist.append(matrix[row][col])
    print("FLIPLIST",fliplist)

    


# a = [
#   [0, -1, -3, 2, 0],
#   [1, -2, -5, -1, -3],
#   [3, 0, 0, -4, -1]
# ]

# b = [
#     [1, 0, 0, -2, -3],
#     [-4, -5, -6, -2, -1],
#     [0, 0, 0, 0, -1],
#     [1, 2, 3, 0, 3]
#   ]

# c = [
#     [-1]
#   ]
# minimumPassesOfMatrix(c)