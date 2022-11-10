'''
Find all sets of combinations that  4 of which sum to the target

🔴 Hard
https://www.algoexpert.io/questions/four-number-sum
'''

def fourNumberSum(array, targetSum):
    sumDict = {}
    ret = []
    for i in range(len(array)):
        # print("INDEX:",array[i])
        # print("j loop range:", range(i+1,len(array)))
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            difference = targetSum - sum
            if difference in sumDict:
                for pair in sumDict[difference]:
                    ret.append(pair + [array[i], array[j]])
        for k in range(0, i):
            sum = array[i] + array[k]
            if sum not in sumDict:
                sumDict[sum] = [[array[k],array[i]]]
            else:
                sumDict[sum].append([array[k], array[i]])
    print(ret)
    return ret



fourNumberSum([7, 6, 4, -1, 1, 2],16)