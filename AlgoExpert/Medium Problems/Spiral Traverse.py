'''
Spiral around a two-dimensional array 
clockwise adding numbers to a new list
🔵 Medium Difficulty

https://www.algoexpert.io/questions/spiral-traverse 
'''


def spiralTraverse(array):
    # Write your code here.
    ret = []
    
    startRow,endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    
    while startRow <= endRow and startCol <= endCol:       
        #TOP ROW
        for col in range(startCol,endCol):
            ret.append(array[startRow][col])
        #RIGHT COL
        for row in range(startRow, endRow + 1):
            ret.append(array[row][endCol])
        #BOTTOM ROW
        for col in reversed(range(startCol,endCol)):
            if startRow == endRow:
                break
            ret.append(array[endRow][col])
        #LEFT COL
        for row in reversed(range(startRow + 1,endRow)):
            if startCol == endCol:
                break
            ret.append(array[row][startCol])
        
        startRow += 1
        endRow -=1
        startCol += 1
        endCol -=1

    # print(ret)
    return ret

        



spiralTraverse([
  [1, 2,   3,  4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9,  8,  7]
])

