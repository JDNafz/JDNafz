global decNum
global incNum
global inc
global dec
global longest

def longestPeak(array):
    # Write your code here.
    longest = 0
    inc = False
    dec = False
    incNum = 0
    decNum = 0

    i=0
    while i < len(array)-1:
        peak = 0
        if array[i] < array [i+1]:
            inc = True
        if array[i] > array[i+1]:
            dec = True
        while inc == True and i < len(array)-1:
            print(array[i], "increase while")

            if array[i] < array[i+1]:
                print("inc!")
                incNum =+ 1
                if dec == True:
                    print("peak found, {} is a peak! incNum is {}".format(array[i], incNum))
                    longest - labelPeak(peak, incNum, decNum)                
                i += 1
                dec = False

            elif array[i] > array[i+1]:
                print("dec!")
                incNum = 0
                decNum += 1
                if i == len(array)-2:
                    print("peak found, {} is a peak! incNum is {}".format(array[i], incNum))
                    longest = labelPeak(peak, incNum, decNum) 
                    print("peak found, {} is a peak! incNum is {}".format(array[i], incNum))
                dec = True
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
            print(array[i], "decrease while")
            if array[i] < array[i+1]:
                print("inc")
                inc = True
                incNum =+ 1
                i+= 1
                print("peak complete, longest:{}, incNum:{}, decNum{}, array[i]:{}".format(longest, incNum, decNum, array[i]))
                longest = labelPeak(peak, incNum, decNum)
                print("peak complete, longest:{}, incNum:{}, decNum{}, array[i]:{}".format(longest, incNum, decNum, array[i]))             
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
        if i == len(array)-2:
            if dec is True:
                print("I'm the last num, longest:{}, incNum:{}, decNum{}, array[i]:{}".format(longest, incNum, decNum, array[i]))
                longest = labelPeak(peak, incNum, decNum)
                print("I'm the last num, longest:{}, incNum:{}, decNum{}, array[i]:{}".format(longest, incNum, decNum, array[i]))     

    print("DONE:",longest)
    return longest

def labelPeak(peak, incNum, decNum):
    longest = max(peak, incNum + decNum)
    peak = incNum + decNum
    incNum = 0
    decNum = 0
    return longest

            
           


# longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
longestPeak([1,3,2])