#  1 - positive
# -1 - negative
#  0 - zero
def minimumPassesOfMatrix(matrix):
    passes = 0
    hasNegative,flip = passThrough(matrix)
    while hasNegative:
        matrix = flipthem(flip,matrix)
        passes += 1
        hasNegative,flip = passThrough(matrix)
        if len(flip) == 0:
            return -1
    
    return passes

def passThrough(matrix):
    flip = {}
    #check everything
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                continue
            #if neg
            if matrix[row][col] < 0:
                neighbors = touching(row,col,matrix)
                for neighbor in neighbors:
                    i,j = neighbor[0],neighbor[1]
                    if matrix[i][j] > 0:
                        flip.add([row,col])
                        break
                    continue
            if neighbors == []:
                return False
    return True, flip

def flipthem(flip,matrix):
    if len(flip) == 0:
        pass
    for pair in flip:
        row, col = pair[0],pair[1]
        matrix[row][col] *= -1
    return matrix

def touching(row,col,matrix):
    neighbors = []
    if col < len(matrix[0]) -1:
        neighbors.append([row][col])
    if row < len(matrix) - 1:
        neighbors.append([row + 1, col])
    if col > 0:
        neighbors.append([row][col + 1])
    if row > 0:
        neighbors.append([row - 1][col])
    return neighbors

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")



a = [
  [0, -1, -3, 2, 0],
  [1, -2, -5, -1, -3],
  [3, 0, 0, -4, -1]
]

minimumPassesOfMatrix(a)