'''
write a binary search method for a given array of integers.


https://www.algoexpert.io/questions/binary-search
'''

'''
I took a less conventional route to solve this one, I used a multiplyer to divide the total length of the array by 2, 4, 6, etc.
if target was higher I add 
'''
def binarySearch(array, target, i=0):
    # Write your code here.
    if target < array[i] or target > array[-1]:
        return -1
    multiplyer = 2
    while array[i] != target:
        if array[i] < target and array[i+1] > target:
            print("-1")
            return -1
        if array[i] < target:
            i = i + len(array)//multiplyer
            multiplyer +=2
        else:
            i =i - len(array)//multiplyer
            multiplyer += 2
    print("found",array[i]," at idx", i)
    return i


# binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33)
# binarySearch([1, 5, 23, 111],35)
# binarySearch([5, 23, 111],3)