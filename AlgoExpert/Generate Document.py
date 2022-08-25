'''
check if there are enough characters in the 
"characters" string to generate the "document" string.

🟢Easy Difficulty
https://www.algoexpert.io/questions/generate-document
'''

def generateDocument(characters, document):
    # Write your code here.
    charCount = {}
    for char in characters:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    for char in document:
        if char in charCount:
            charCount[char] -= 1
            if charCount[char] < 0:
                return False
        else:
            return False

    return True



generateDocument("aaabc","abc")
