
from Chess import *

# moveBishop(numberOfInput,bothCoordinates)

inputList = []

#write a file with all possible inputs
#run the file in the main app enter "4096" manually then paste the inputs
with open("Output.txt", "w") as text_file:

    #for keys and Values in dict, pair each key with every other key
    for keyA,valA in mapping.items() :
        for keyB,valB in mapping.items():
            
            text_file.write(keyA + " " + keyB + "\n")






