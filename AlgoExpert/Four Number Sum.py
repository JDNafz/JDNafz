def fourNumberSum(array, targetSum):
    sumDict = {}
    ret = []
    for i in range(len(array)):
        print("INDEX:",array[i])
        print("j loop range:", range(i+1,len(array)))
        for j in range(i+1,len(array)):
            sum = array[i] + array[j]
            print("sum",sum)
            if sum in sumDict:
                #key is the sum, value is an array of indexes in the main array to add together
                sumDict[sum].append([i,j])
            else:
                sumDict[sum] = [[i,j]]
            currentMissingSum = targetSum - (array[i] + array[j])
            if currentMissingSum in sumDict:
                pass
    print(ret)
    return ret



fourNumberSum([7, 6, 4, -1, 1, 2],16)