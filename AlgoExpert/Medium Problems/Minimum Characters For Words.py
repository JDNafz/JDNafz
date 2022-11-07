'''
🔵 Medium
https://www.algoexpert.io/questions/minimum-characters-for-words
'''

def minimumCharactersForWords(words):
    maxUsed = {}
    for word in words:
        letters = {}
        for i in range(len(word)):
            currLetter = word[i]
            if currLetter not in letters:
                letters[currLetter] = 1
            else:
                letters[currLetter] += 1
            if currLetter not in maxUsed:
                maxUsed[currLetter] = letters[currLetter]
            if letters[currLetter] > maxUsed[currLetter]:
                maxUsed[currLetter] = letters[currLetter]
    
    output = []
    for key in maxUsed:
        for _ in range(maxUsed[key]):
            output.append(key)
    # print(output)
    return output



test1 = ["this", "that", "did", "deed", "them!", "a"]
#Result ["t","t","h","i","s","a","d","d","e","e","m","!"]
minimumCharactersForWords(test1)