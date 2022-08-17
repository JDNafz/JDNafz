
# [1, 2, 5]

def nonConstructibleChange(coins):
    constructibleTotal = 0
    coins.sort()
    
    for i in range(len(coins)):
        print("the coin is", coins[i])

        # if it's the last coin
        if i == len(coins)-1:
            if constructibleTotal < coins[i]:
                constructibleTotal += coins[i]
        else:
            if constructibleTotal < coins[i+1]:
                constructibleTotal += coins[i]
                print("ConsTotal is", constructibleTotal)
    print ("Final answer:", constructibleTotal+1)
    return constructibleTotal+1
            
# in order[1, 1, 2, 3, 5, 7, 22]            



list20 =   [5, 7, 1, 1, 2, 3, 22] #20
list4 = [1,2,5] # 4
list6 = [1,1,1,1,1] # 6

nonConstructibleChange(list6)

