visited = {}
def largestRange(array):
    if len(array) == 1:
        print("TOTAL:", [array[0], array[0]] )
        return [array[0], array[0]]
    longestDistance = 0
    longest = []
    for num in array:
        if num not in visited:
            visited[num] = False
    for num in array:
        Currlongest = []
        if visited[num] == False:
            Currlongest = [num, num]
            Currlongest = searchNum(num, Currlongest)
            CurrDistance = Currlongest[1] - Currlongest[0]
            if CurrDistance > longestDistance:
                longestDistance = CurrDistance
                longest = Currlongest
    print("TOTAL:", longest, "length of longest:", len(longest))
    return longest
            
def searchNum(num, Currlongest):
    if visited[num] == False:
        visited[num] = True
        
        lower, higher = num - 1, num + 1
        if lower in visited:
            if lower < Currlongest[0]:
                Currlongest[0] = lower
            Currlongest = searchNum(lower, Currlongest)
        if higher in visited:
            if higher > Currlongest[1]:
                Currlongest[1] = higher
            Currlongest = searchNum(higher, Currlongest)
    return Currlongest


test2 = [1]
# largestRange(test2)

test3 = [1, 2]
# largestRange(test3)

test9 = [0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]
# largestRange(test9)

test10 = [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]
# largestRange(test10)

test12 = [-1, 0, 1]
largestRange(test12)
        