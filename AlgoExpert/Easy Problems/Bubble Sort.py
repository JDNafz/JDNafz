'''
Perform a bubble sort

🟢 Easy Difficulty
https://www.algoexpert.io/questions/bubble-sort 
'''


def bubbleSort(array):
    # Write your code here.

    while True:
        print(array)
        global swap
        swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap = True
        if swap == False:
            break
    return array

