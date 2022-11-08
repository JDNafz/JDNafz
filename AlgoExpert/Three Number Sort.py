'''
Sort the numbers into the order matching the 'order' array using constant space.

🔵 Medium
https://www.algoexpert.io/questions/three-number-sort
'''
def threeNumberSort(array, order):
    index = 0 
    for idx in range(len(array)):
        if array[idx] == order[0]:
            array[index], array[idx] = array[idx], array[index]
            index += 1
    index = len(array) - 1
    for idx in range(len(array)-1, -1, -1): # range(find last idx of array, include idx 0, increment by -1)
        if array[idx] == order[2]:
            array[index], array[idx] = array[idx], array[index]
            index -= 1
    # print(array)
    return array






array1 = [1, 0, 0, -1, -1, 0, 1, 1]
order1 = [0, 1, -1]
threeNumberSort(array1,order1)