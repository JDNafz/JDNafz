"""""
https://open.kattis.com/problems/chess


The basic premise of this code is to calculate how a bishop 
would move from any given position on the chessboard to any 
other position. Check out the full description of the coding 
challenge here: https://open.kattis.com/submissions/9221963

"""

#TODO: Re map the coordinate plane to clean up code and readability
#This is done and working, but I may come back and clean it up more!

#mapping created on chess board 
    #A 1 is   [0    ,  [0      , 0            ]] Black
    #A 8 is   [1    ,  [0      , 0            ]] White
    #         [Color, [up/down, distanct right]]
mapping = {
    "A 1" : [0,[0,0]],
    "B 2" : [0,[0,1]],
    "C 3" : [0,[0,2]],
    "D 4" : [0,[0,3]],
    "E 5" : [0,[0,4]],
    "F 6" : [0,[0,5]],
    "G 7" : [0,[0,6]],
    "H 8" : [0,[0,7]],
    
    "C 1" : [0,[-1,1]],
    "D 2" : [0,[-1,2]],
    "E 3" : [0,[-1,3]],
    "F 4" : [0,[-1,4]],
    "G 5" : [0,[-1,5]],
    "H 6" : [0,[-1,6]],

    "E 1" : [0,[-2,2]],
    "F 2" : [0,[-2,3]],
    "G 3" : [0,[-2,4]],
    "H 4" : [0,[-2,5]],

    "G 1" : [0,[-3,3]],
    "H 2" : [0,[-3,4]],

    "A 3" : [0,[1,1]],
    "B 4" : [0,[1,2]],
    "C 5" : [0,[1,3]],
    "D 6" : [0,[1,4]],
    "E 7" : [0,[1,5]],
    "F 8" : [0,[1,6]],

    "A 5" : [0,[2,2]],
    "B 6" : [0,[2,3]],
    "C 7" : [0,[2,4]],
    "D 8" : [0,[2,5]],

    "A 7" : [0,[3,3]],
    "B 8" : [0,[3,4]],

    #white squares
    "A 8" : [1, [0,0]],
    "B 7" : [1, [0,1]],
    "C 6" : [1, [0,2]],
    "D 5" : [1, [0,3]],
    "E 4" : [1, [0,4]],
    "F 3" : [1, [0,5]],
    "G 2" : [1, [0,6]],
    "H 1" : [1, [0,7]],
    
    "A 6" : [1, [-1,1]],
    "B 5" : [1, [-1,2]],
    "C 4" : [1, [-1,3]],
    "D 3" : [1, [-1,4]],
    "E 2" : [1, [-1,5]],
    "F 1" : [1, [-1,6]],

    "A 4" : [1, [-2,2]],
    "B 3" : [1, [-2,3]],
    "C 2" : [1, [-2,4]],
    "D 1" : [1, [-2,5]],

    "A 2" : [1, [-3,3]],
    "B 1" : [1, [-3,4]],

    "C 8" : [1, [1,1]],
    "D 7" : [1, [1,2]],
    "E 6" : [1, [1,3]],
    "F 5" : [1, [1,4]],
    "G 4" : [1, [1,5]],
    "H 3" : [1, [1,6]],

    "E 8" : [1, [2,2]],
    "F 7" : [1, [2,3]],
    "G 6" : [1, [2,4]],
    "H 5" : [1, [2,5]],

    "G 8" : [1, [3,3]],
    "H 7" : [1, [3,4]],
}


def moveBishop(numberOfInput,coordinateInputList):

    for i in range(numberOfInput):
        numMoves = 0

        CoordinateHolder = coordinateInputList[i]

        #Convert A 1 to [0, [0,0]] etc
        startCoordinate = mapping[CoordinateHolder[0:3]]
        endCoordinate = mapping[CoordinateHolder[4:7]]

        #put the starting coordinate into the outputString
        outputString = CoordinateHolder[0:3]

        #if going to same location
        if startCoordinate[1] == endCoordinate[1]:
            numMoves = 0
        #if if row or col is the same
        elif startCoordinate[1][0] == endCoordinate[1][0] or startCoordinate[1][1] == endCoordinate[1][1]:
            outputString += " " + CoordinateHolder[4:7]
            numMoves = 1

        else:
            numMoves = 2
            # # find the linking move
            # print("START",startCoordinate, "END:", endCoordinate)
            if [startCoordinate[0],[startCoordinate[1][0],endCoordinate[1][1]]] in list(mapping.values()):
                # for the key and value pairings in the dict
                for key,val in mapping.items() :
                    # if current value == possible coordinate 
                    if val == [startCoordinate[0],[startCoordinate[1][0],endCoordinate[1][1]]]: 
                        outputString += " " + key
                        # print(startCoordinate[0],[startCoordinate[1][0],endCoordinate[1][1]])

            else:
                for key,val in mapping.items() :
                    if val == [startCoordinate[0],[endCoordinate[1][0],startCoordinate[1][1]]]:
                        outputString += " " + key

            #add final destination to outputString
            outputString += " " + CoordinateHolder[4:7]
            
        # if color is different
        if mapping[CoordinateHolder[0:3]][0] != mapping[CoordinateHolder[4:7]][0]:
            print("Impossible")
        else:
            print(str(numMoves),outputString)


if __name__ == "__main__":
    #How many tests should be done?
    numberOfInput = int(input())     

    #initialize 
    inputCoordinates = []

    for i in range(numberOfInput):
        #Take in all the inputs into a list
        inputCoordinates.append(input())
    moveBishop(numberOfInput,inputCoordinates)

#note to self, clean code up before submitting it, review every comment.