def fourNumberSum(array, targetSum):
    sumDict = {}

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
    print(sumDict)
    for key in sumDict:

        pass



        # print("k loop range:", range(0,i))
        # for k in range(0,i):
        #     print("k:{}".format(array[k]))


fourNumberSum([7, 6, 4, -1, 1, 2],16)