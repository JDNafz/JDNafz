
def longestPeak(array):
    # Write your code here.

    for i in range(1,len(array)-1):
        if array[i-1] < array[i] > array[i+1]:
            print("peak found, min array is {},{},{}".format(array[i-1],array[i], array[i+1]))
            peak = findPeakDistance(array,i)
        if array[i] < array[i + 1]:
            print("{} < {}".format(array[i],array[i+1]))
        elif array[i] > array[i +1]:
            print("{} >{}".format(array[i], array[i+1]))
        else:
            print("{} == {}".format(array[i],array[i+1]))


def findPeakDistance(array, idx):
    length = 1
    for i in reversed(range(idx)):
        if array[i] > array[i+1]





longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
# longestPeak([1,3,2])