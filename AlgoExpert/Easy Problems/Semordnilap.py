'''
Semordnilap is the other side of the palindrome for "palindromes" ie. "palindromessemordnilap"
Check through the list to and return words in pairs if they have a matching palindrome.

🟢 Easy Difficulty
https://www.algoexpert.io/questions/semordnilap
'''
def semordnilap(words):
    reversedWords = []
    outputList = []
    for word in words:
        if word in reversedWords:
            outputList.append([word, reverseIt(word)])
            continue
        else:
            reversedWords.append(reverseIt(word))

    print("outputList = ", outputList)
    return outputList

def reverseIt(word):
    revWordTemp = ""
    for char in reversed(word):
        revWordTemp += char
    return revWordTemp 


test1 = ["dog", "god"]
semordnilap(test1)