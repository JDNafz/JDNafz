'''
Find the min wait time for queries in an array.
basically apply the current query length to all the following items, add them up.
item * theNumberOfItemsLeft + totaltime = new total wait time.

https://www.algoexpert.io/questions/minimum-waiting-time
🟢 Easy Difficulty
'''
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    waitTime = 0
    for idx, item in enumerate(queries,start = 1):
        queriesleft = len(queries) - idx
        waitTime += item * queriesleft
    return waitTime
    
    
