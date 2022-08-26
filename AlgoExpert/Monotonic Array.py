'''
Check if array is Monotonic. If it only increases or/and 
stays the same  --- OR ----  decreases and/or stays the same.

🔵 Medium Difficulty
https://www.algoexpert.io/questions/monotonic-array
'''


def isMonotonic(array):
    # Write your code here.
    for i in range(len(array)-1):
        if array[i] < array[len(array)-1]:
            if array[i] > array[i+1]:
                print("False")
                return False
        elif array[i] > array[len(array)-1]:
            if array[i] < array[i+1]:
                print("False2")
                return False
        else:
            if array[i] != array[i+1]:
                print("False3")
                return False
    print("True")
    return True

isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])