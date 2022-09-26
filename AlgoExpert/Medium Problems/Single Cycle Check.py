'''
each index indicates moving forward or backwards in the array, if the
create a cycle then return true.

🔵 Medium
https://www.algoexpert.io/questions/single-cycle-check
'''

def hasSingleCycle(array):
    counter,idx = 0,0
    while counter < len(array):
        if array[idx] == float("inf"):
            break
        array[idx],idx,counter = float("inf"), (idx + array[idx]) % len(array), counter + 1

    if idx == 0 and counter == len(array):
        return True
    return False




# hasSingleCycle([2, 3, 1, -4, -4, 2])
# hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 909, -26])
hasSingleCycle([0, 1, 1, 1, 1])