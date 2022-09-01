from cProfile import label

global longest
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
        print(array[i])
        if array[i] < array [i+1]:
            inc = True
            incNum += 1
            i += 1
        else:
            inc = False
        while inc == True and i < len(array)-1:
            print(array[i], inc)

            if array[i] < array[i+1]:
                print("inc")
                incNum =+ 1
                if dec == True:
                    print("peak^^^")
                    labelPeak(peak, firsthalf, decNum)                
                i += 1
                dec = False

            elif array[i] > array[i+1]:
                print("dec")
                firsthalf = incNum
                incNum = 0
                decNum += 1
                dec = True
                if inc == True:
                    inc = False
                i += 1

            else:
                print("same")
                incNum = 0
                if dec == True:
                    print("to the top")
                    labelPeak(peak,firsthalf,decNum)
                decNum = 0
                i += 1
                inc = False
                dec = False

        while dec == True and i < len(array)-1:
            print(array[i], inc)
            if array[i] < array[i+1]:
                print("inc")
                incNum =+ 1
                if dec == True:
                    print("peak^^^")
                    labelPeak(peak, firsthalf, decNum)                
                i += 1
                dec = False
            elif array[i] > array[i+1]:
                print("dec")
                firsthalf = incNum
                incNum = 0
                decNum += 1
                dec = True
                if inc == True:
                    inc = False
                i += 1
            else:
                print("same")
                incNum = 0
                if dec == True:
                    print("to the top")
                    labelPeak(peak,firsthalf,decNum)
                decNum = 0
                i += 1
                inc = False
                dec = False

    print("DONE:",longest)
    print("peak:",peak)
    return longest

def labelPeak(peak, firsthalf, decNum):
    longest = max(peak,firsthalf + decNum)
    peak = firsthalf + decNum
    return longest


longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
