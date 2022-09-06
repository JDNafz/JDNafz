'''
Merge overlapping intervals in an array of intervals

🔵 Medium Difficulty
https://www.algoexpert.io/questions/merge-overlapping-intervals
'''


def mergeOverlappingIntervals(intervals):
    intervals.sort()
    start = intervals[0][0]
    end = intervals[0][1]
    i = 1
    endPoint = len(intervals)
    while i < endPoint:
        if intervals[i][0] <= end:
            intervals[i-1] = [start,max(end,intervals[i][1])]
            del intervals[i]
            endPoint -= 1
            i -= 1
        start,end = intervals[i][0], intervals[i][1]
        i += 1 
    print(intervals)
    return intervals



# mergeOverlappingIntervals([
#     [43, 49],
#     [9, 12],
#     [12, 54],
#     [45, 90],
#     [91, 93]
#   ]) 

mergeOverlappingIntervals( [
    [1, 22],
    [-20, 30]
  ])