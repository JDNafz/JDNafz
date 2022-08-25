'''
count the repeated characters in a string, 
denoting a number 1-9 for each occurance, 
then the character. 
ie. "AAAAAAAAAAAAABBCCCCDD"
returns "9A4A2B4C2D"
9As, 4As, 2Bs 4Cs 2Ds and not
13A


🟢Easy Difficulty
https://www.algoexpert.io/questions/run-length-encoding
'''


def runLengthEncoding(string):
    # Write your code here.
    outString = ""
    counter = 1
    if len(string) == 1:
        return str(1) + string
    for char in range(len(string)-1):
        if string[char] != string[char+1]:
            outString += str(counter) + string[char]
            counter = 1
            if char == len(string)-2:
                outString += str(counter) + string[char+1]
        #if were at the second to last char and it's the same as the last.
        elif char == len(string)-2:
            counter += 1
            if counter > 9:
                outString += "9" + string[char]
                counter -= 9
            outString += str(counter) + string[char]
        else:
            counter += 1
            if counter > 9:
                outString += "9" + string[char]
                counter -= 9
    return outString


runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
