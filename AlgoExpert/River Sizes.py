def riverSizes(matrix):
    array = []
    for row in matrix:
        for col in matrix:
            if matrix[row][col] == 1:
                riverLength = 1
                searchRiver(row,col,matrix,array,riverLength)
    print(array)
    return array

def searchRiver(row,col,matrix,array,riverLength):
    riverLength += 1
    matrix[row][col] = -1

    if 1 < row < len(matrix[-1]):
        searchRiver(row+1, col,   matrix,array,riverLength)
        searchRiver(row-1, col,   matrix,array,riverLength)
    if 1 < col < len(matrix[1][0]):
        searchRiver(row,   col+1, matrix,array,riverLength)
        searchRiver(row,   col-1, matrix,array,riverLength)

    if col == 1 and : 
        searchRiver(row,col,matrix,array)
    return
