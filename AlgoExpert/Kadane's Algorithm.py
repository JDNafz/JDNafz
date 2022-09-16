'''
Find the max sum of any given subarray in an array.

🔵 Medium
https://www.algoexpert.io/questions/kadane's-algorithm
'''

def kadanesAlgorithm(array):
    largestSum = float("-inf")
    currentSum = 0
    for value in array:
        currentSum += value
        if currentSum >= largestSum:
            largestSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return largestSum


# kadanesAlgorithm([0,1,2,3,4,-200,3,4,5,6,-200])
# kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])