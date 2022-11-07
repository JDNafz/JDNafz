'''
🔵 Medium Difficulty
https://www.algoexpert.io/questions/reverse-words-in-string
'''
def reverseWordsInString(string):
    word = ''
    sentence = []
    for char in string:
        if word == ' ':
            sentence.insert(0, ' ')
            word = ''
        if char == ' ':
            sentence.insert(0, word)
            word = ''
        word += char
    sentence.insert(0,word)
    outString = ''
    for word in sentence:
        outString += word

    return outString

string = "AlgoExpert is the best!"
reverseWordsInString(string)