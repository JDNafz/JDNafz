
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

    
binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33)
