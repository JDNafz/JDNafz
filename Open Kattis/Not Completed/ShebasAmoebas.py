'''
Given an image of an amoeba, calculate how many 
independent loops are formed into amoebas.


https://open.kattis.com/problems/amoebas
'''
#UNFINISHED NOT SUBMITTED YET
#TODO: Review all code and submit

# xInput = input()

xInput = str('4 4') #Hardcoded Number of Rows and Colums

#This will read the input and determine the integers
for i in range(len(xInput)):
    if ord(xInput[i]) == 32:
        numberOfRows = int(xInput[0:(i)])
        numberOfColums = int(xInput[i+1:(len(xInput))])
#Notes for self: ord('x') returns the numeric ascii value of x
# Can I improve this code using .split ?

grid = [[row, col] for row in range(numberOfRows) for col in range(numberOfColums)]




#Assign colors to coordinates
rowCounter = 0
k = 0
while rowCounter < numberOfRows:
    currentRow = input()
    for i in range(len(currentRow)):        
        grid[k].append((currentRow[i]))
        k+=1
    rowCounter+=1




#TEST to check current state of grid colors
def printGrid():
    print("---------")
    k = 0
    for i in range(numberOfRows):
        for j in range(numberOfColums):
            print(grid[k][2],end='')
            k += 1
        print('\n')

# change '#' into '$' After reading them. to cicle through.
# {[x,y,color],[i,j,color],[i,j,color]}
def findLoop():
    for i in range(len(grid)):        
        if grid[i][2] == '#':
            grid[i][2] = '$'
            # if grid[i][2] == '$':
            while grid[i][1] != (numberOfColums - 1): #if its not on an end
                isRight(i)
                i+=1  # is this being use correctly?
                    
            isBelowLeft(i)
            printGrid()
            print("break")
            break           

def isRight(i):

    if grid[i+1][2] == '#': 
        grid[i+1][2] = 'B' 
        i += 1 #used to exit loop
    else:
        i += 1

def isBelowLeft(i):
    print("enter is left function")
    print(grid[i])
    if grid[i][1] != 0: #if not in the first position of the row 

        if grid[i][0] != numberOfRows - 1: #if not in bottom row
            print(grid[i], "is not in first row or bottom row")
            if grid[i + numberOfColums - 1][2] == '#':
                grid[i + numberOfColums - 1][2] = 'L'
                i = (i + numberOfColums - 1)
            else:
                print("Looked for # and found", grid[i], "in bounds and ")            
        else:
            print(i,"+", numberOfColums, "=", (i+numberOfColums)," is greater than the total range of",(numberOfColums*numberOfRows))

#TODO: EliSabeth wants you to know what this is cause it is relevant and cool
# if(NAME=="MAIN"):
#     print("Bleh")


print("Original Input Above ---------------------------------")
findLoop()

#PRINT FINAL ANSWER
endCount = 0
for i in range(len(grid)):  
    if grid[i][2] == "$":
        endCount +=1
print("endCount =", endCount)
'''
https://open.kattis.com/problems/amoebas

sample input:

###.
.###
####
..#.

Create dictionary from [x,y,z] elements
Dict[(row,col)] = '#'
if (0,0) is in dict then check it.

for value in grid:
    #value is same as grid[i]
    #         [x]      [y]         [z]
    dict[value[0],value[1]] = value[2]
'''