'''
Find the max sum of an array, without adding neighboring integers.

🔵 Medium Difficulty


https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
'''


def maxSubsetSumNoAdjacent(array):
    currentMax, previousMax = 0, 0
    for number in array:
        previousMax, currentMax = currentMax, max(currentMax, previousMax + number)
    return currentMax

#start to conceptualize by thinking of a new array of max values

# [7, 10, 12,  7,  9, 14] GIVEN ARRAY
#  ^   ^   ^   ^   ^   ^
# [7, 10, 19, 19, 28, 33] Checking the max of each number 


# [7,             10,             n,                       ] 
#  ^previous max   ^current max    ^next "number" in array
#                  ^will always become previousMax once n is assigned 'previousMax = currentMax'
#                                   ^becomes currentmax by checking if previousMax + "number" is larger than current max


"""
#optionally store a 3rd variable like so:

def maxSubsetSumNoAdjacent(array):
    # Write your code here.

    currentMax, previousMax = 0, 0
    #for each element in the array
    for number in array:
        tempMax = max(currentMax, previousMax + number)
        previousMax = currentMax
        currentMax = tempMax

    return currentMax

"""


test1 = [75, 105, 120, 75, 90, 135]

if maxSubsetSumNoAdjacent(test1) == 330:
    print("passed test1")