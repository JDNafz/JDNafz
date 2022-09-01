def fourNumberSum(array, targetSum):

    sumDict = {}
    for i in range(len(array)-1):
        sum = array[i] + array[i+1]
        if sum in sumDict:
            sumDict[sum].append([array[i],array[i+1]])
        else:
            sumDict[sum] = [[array[i],array[i+1]]]
    print(sumDict)