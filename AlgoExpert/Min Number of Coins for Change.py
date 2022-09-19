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
            # print("Amount:{}, denomination:{}".format(amount, d), numCoins)
    if numCoins[n] != float("inf"):
        return numCoins[n]
    return -1    





minNumberOfCoinsForChange(9, [3,5])