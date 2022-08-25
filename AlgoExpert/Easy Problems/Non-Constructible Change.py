'''
Given n number of coins and their values. 
Find the smallest amout of change that is not possible to create.
i.e. 1cent-coin, 2cent-coin,5cent-coin. > cannot make 4cents change.
If there was another 1-cent coin in the list you could make up to 9cents of change.

🟢 Easy Difficulty

https://www.algoexpert.io/questions/non-constructible-change
'''

def nonConstructibleChange(coins):
    # Write your code here.

    constructibleTotal = 0
    coins.sort()

    for i in range(len(coins)):
        # if it's the last coin
        if i == len(coins)-1:
            #if also happens to be the first coin (which is 1)
            if constructibleTotal+1 == coins[i]:
                    #add the single coin to the total
                    constructibleTotal += coins[i]
            elif constructibleTotal >= coins[i]:
                constructibleTotal += coins[i]
        else:
            #exception if its the first coin
            if constructibleTotal == 0:
                constructibleTotal += coins[i]
            elif constructibleTotal >= coins[i]-1:
                constructibleTotal += coins[i]

            # else: 
    #           print("constructible total is",constructibleTotal,"and should didn't make it to coin:", coins[i+1])


    return constructibleTotal+1
            
     
'''
Test cases of my own in VS Code

list20 =   [5, 7, 1, 1, 2, 3, 22] #20
list4 = [1,2,5] # 4
list6 = [1,1,1,1,1] # 6
list2 = [1]
nonConstructibleChange(list2)

'''