'''

🔵 Medium
Needs review, brushed over this too fast.
'''

def minNumberOfCoinsForChange(n, denoms):    
    numCoins = [0] + [float("inf") for _ in range(n)]
    
    for d in denoms:
        #amount represents $ amount in the array from 0-n attempting to build towards
        for amount in range(len(numCoins)):
            if d <= amount:
                numCoins[amount] = min(numCoins[amount], numCoins[amount -d] + 1)
    if numCoins[n] != float("inf"):
        return numCoins[n]
    return -1    





minNumberOfCoinsForChange(9, [3,5])