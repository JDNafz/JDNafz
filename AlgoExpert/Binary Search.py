
def binarySearch(array, target, i=0):
    # Write your code here.

    multiplyer = 2
    
    while array[i] != target:
        if array[i] < target and array[i+1] > target:
            return -1
        if array[i] < target:
            i = i + len(array)//multiplyer
            multiplyer +=2

        else:
            i =i - len(array)//multiplyer
            multiplyer += 2
    print(i)
    return i

binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33)
