'''
Move all instance of selected element to the end of the array
🔵 Medium Difficulty
https://www.algoexpert.io/questions/move-element-to-end
'''


def moveElementToEnd(array, toMove):
    # Write your code here.
    right = len(array)-1
    i = 0
    while i < right:
        print(array,i,right)
        if array[i] == toMove:
            while array[right]== toMove:
                right -=1
                if right == i:
                    break
            array[right],array[i] = array[i],array[right]
            right -=1
        i += 1
    print(array)
    return array
