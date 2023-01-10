'''
find is a subarray contains a sum of zero
if so return True

🔵 Medium Difficulty
https://www.algoexpert.io/questions/zero-sum-subarray
'''


def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False


test1 = [4, 2, -1, -1, 3]
zeroSumSubarray(test1)