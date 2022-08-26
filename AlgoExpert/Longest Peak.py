def longestPeak(array):
    # Write your code here.
    longest = 0
    global inc
    inc = False
    global dec
    dec = False
    incNum = 0
    decNum = 0

    i=0
    while i < range(len(array-1)):
        if array[i] < array [i+1]:
            inc = True
        while inc == True:
            if array[i] < array[i+1]:
                incNum =+ 1
                i += 1
            elif array[i] > array[i+1]:
                firsthalf = incNum + 1
                dec = True
                i += 1
            else:
                inc = False
                incNum = 0
            if dec == True:



            
           
    print(longest)
    return longest

longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])