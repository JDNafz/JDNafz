'''
Find the maxium number of ways to make change for a given total amount.
total amount and denominations are assumed to be integers.

🔵 Medium
https://www.algoexpert.io/questions/number-of-ways-to-make-change
'''
def numberOfWaysToMakeChange(n, denoms):
    ways = [1] + [0 for _ in range(n)]
    for denom in denoms:
        for change in range(denom,n+1):
                ways[change] += ways [change - denom]
    print(ways[n])
    return ways[n]

numberOfWaysToMakeChange(10000,[1, 4, 10, 25, 100,500,1000,2000])