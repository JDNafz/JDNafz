'''
Write a function that takes in an array of strings and grousp them into 
Anagrams

🔵 Medium Difficulty
https://www.algoexpert.io/questions/group-anagrams

'''
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedword = "".join(sorted(word))
        if sortedword in anagrams:
            anagrams[sortedword].append(word)
        else:
            anagrams[sortedword] = [word]
    # print(list(anagrams.values()))
    return list(anagrams.values())