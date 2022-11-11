'''
Sort Find the (middle) section of the array that needs to be sorted
return [idx_start, idx_end] of section to be sorted.
🔴 Hard
https://www.algoexpert.io/questions/subarray-sort
'''
def subarraySort(array):
    smolboi = float('inf')
    bigboi = float("-inf")
    for idx in range(1, len(array)):
        # print(array[idx])
        if array[idx - 1] > array[idx]:
            if array[idx] < smolboi: 
                smolboi = array[idx] 
            if array[idx -1] > bigboi:
                bigboi = array[idx -1]
    print(smolboi,bigboi)
    start, end = -1, -1
    for idx in range(len(array)):
        if start == -1:
            if smolboi < array[idx]:
                # print(array[idx],"!")
                start = idx
        if bigboi > array[idx]:
            end = idx

    print([start, end])
    return [start, end]

test15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2]
# subarraySort(test15)

test1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# subarraySort(test1)


test2 = [2, 1]
# subarraySort(test2)