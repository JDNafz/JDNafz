'''
See website for description.

🔵 Medium Difficulty
https://www.algoexpert.io/questions/sunset-views

'''


# def sunsetViews(buildings, direction):
#     maxHeight = 0
#     hasView = []
#     if direction == "WEST":
#         for i in range(len(buildings)):
#             if buildings[i] > maxHeight:
#                 hasView.append(i)
#                 maxHeight = buildings[i]
#     else:
#         for i in reversed(range(len(buildings))):
#             if buildings[i] > maxHeight:
#                 hasView.insert(0,i)
#                 maxHeight = buildings[i]
#     return hasView


#refactored solution to avoid using extra O(n) space by avoiding reversed()
def sunsetViews(buildings, direction):
    result = []
    n = len(buildings)
    maxValue = 0
    
    for idx in range(n - 1, -1, -1) if direction == "EAST" else range(0, n, 1):
        if buildings[idx] > maxValue:
            maxValue = buildings[idx]
            result.append(idx)

    return result[::-1] if direction == "EAST" else result 



b1 = [3, 5, 4, 4, 3, 1, 3, 2]
d1 = "EAST"
# sunsetViews(b1,d1)

test = [i for i in range(10)]
print(test)
