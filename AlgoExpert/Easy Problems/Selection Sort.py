'''
Sort by going through each index, and replacing it with the smallest item that follows.

🟢Easy Difficulty
https://www.algoexpert.io/questions/selection-sort
'''

def selectionSort(array):
    # Write your code here.

    # go over the array once.
    for i in range(len(array)-1):
        #find the smolboi and replace it with the current position in the main loop.
        smolboi = i
        for j in range(i+1, len(array)):
            if array[smolboi] > array[j]:
                smolboi = j
        array[i], array[smolboi] = array[smolboi], array[i]

    print("done:",array) 
    return array



selectionSort([8, 5, 2, 9, 5, 6, 3])