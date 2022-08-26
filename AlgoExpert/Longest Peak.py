from cProfile import label


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
    while i < len(array)-1:
        peak = 0
        if array[i] < array [i+1]:
            inc = True
        while inc == True:
            if array[i] < array[i+1]:
                incNum =+ 1
                if dec == True:
                    labelPeak(peak, firsthalf, decNum)                  
                i += 1
            elif array[i] > array[i+1]:
                firsthalf = incNum
                incNum = 0
                decNum += 1
                dec = True
                i += 1
            else:
                inc = False
                incNum = 0
                if dec == True:
                    labelPeak(peak,firsthalf,decNum)
                decNum = 0
                i+= 1
    print(longest)
    return longest

def labelPeak(peak, firsthalf, decNum):
    longest = max(peak,firsthalf + decNum)
    peak = firsthalf + decNum

            
           


longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])