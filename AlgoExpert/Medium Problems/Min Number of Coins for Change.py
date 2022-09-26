'''

🔵 Medium
Needs review, brushed over this too fast.
'''

def minNumberOfCoinsForChange(n, denoms):    
    numCoins = [0] + [float("inf") for _ in range(n)]
    
    for d in denoms:
        #amount represents $ amount in the array from 0-n attempting to build towards
        for amount in range(d, n+1):
            numCoins[amount] = min(numCoins[amount], numCoins[amount -d] + 1)
            # This print statement clearly shows how to loops work.
            print("Amount:{}, denomination:{}".format(amount, d), numCoins)
    if numCoins[n] != float("inf"):
        return numCoins[n]
    return -1    





minNumberOfCoinsForChange(9, [3,5])
#print statement:
# Amount:3, denomination:3 [0, inf, inf, 1, inf, inf, inf, inf, inf, inf]
# Amount:4, denomination:3 [0, inf, inf, 1, inf, inf, inf, inf, inf, inf]
# Amount:5, denomination:3 [0, inf, inf, 1, inf, inf, inf, inf, inf, inf]
# Amount:6, denomination:3 [0, inf, inf, 1, inf, inf, 2, inf, inf, inf]
# Amount:7, denomination:3 [0, inf, inf, 1, inf, inf, 2, inf, inf, inf]
# Amount:8, denomination:3 [0, inf, inf, 1, inf, inf, 2, inf, inf, inf]
# Amount:9, denomination:3 [0, inf, inf, 1, inf, inf, 2, inf, inf, 3]
# Amount:5, denomination:5 [0, inf, inf, 1, inf, 1, 2, inf, inf, 3]
# Amount:6, denomination:5 [0, inf, inf, 1, inf, 1, 2, inf, inf, 3]
# Amount:7, denomination:5 [0, inf, inf, 1, inf, 1, 2, inf, inf, 3]
# Amount:8, denomination:5 [0, inf, inf, 1, inf, 1, 2, inf, 2, 3]
# Amount:9, denomination:5 [0, inf, inf, 1, inf, 1, 2, inf, 2, 3]