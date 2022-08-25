'''
If a character in the string is not repeated 
later in the string, return the first one.

Easy Difficulty
https://www.algoexpert.io/questions/first-non-repeating-character
'''


def firstNonRepeatingCharacter(string):
    # Write your code here.
    
    charList = {}
    for i in range(len(string)):
        #if key was reapeated we no longer need the index marked > mark it corn.
        if string[i] in charList:
            charList[string[i]] = "It's Corn"
        #has not been repeated > note the index
        else:
            charList[string[i]] = i
        
    for j in range(len(string)):
        #if it 
        if charList[string[j]] != "It's Corn":
            return charList[string[j]]
    return -1
