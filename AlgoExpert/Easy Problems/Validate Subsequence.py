'''
🟢 Easy Difficulty
https://www.algoexpert.io/questions/validate-subsequence
'''
def isValidSubsequence(array, sequence):
    j = 0;
    for i in range(len(array)):
        if array[i] == sequence[j]:
            j += 1;
            if j == len(sequence):
                return True;
    return False