'''
Find the longest peak in an array. Peak distance is 
set by continual decrease in both directions from the peak.

🔵 Medium Difficulty

https://www.algoexpert.io/questions/longest-peak
'''
'''

'''
def longestPeak(array):
    # Write your code here.
    peak = 0
    i = 1
    while i < len(array)-1:
        # print(array[i])
        if array[i-1] < array[i] > array[i+1]:
            # print("peak found, min array is {},{},{}".format(array[i-1],array[i], array[i+1]))
            recentPeak,skip = findPeakDistance(array,i)
            peak = max(recentPeak, peak)
            i += skip
        else:
            i += 1
    print(peak)
    return peak

def findPeakDistance(array, idx):
    length = 1
    skip = 1
    # print("i < idx")
    for x in reversed(range(0, idx)):
        # print(array[x], "<", array[x+1])
        if array[x] < array[x + 1]:
            length += 1
            # print("disney")
        else:
            break

    # print("idx > i")
    for x in range(len(array)- idx-1):
        # print(array[x+idx], "& ", array[x+idx+1])
        if array[x+idx] > array[x + 1 + idx]:
            length += 1
            skip += 1
            # print("mark")
        else:
            break
 
    # print("length:",length)
    return length, skip




longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])


# longestPeak([1,3,5,4,2])