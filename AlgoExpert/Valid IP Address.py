def validIPAddresses(string):
    
    #find first number
    checklist = find1stnum(string)
    # plist(checklist)

    #find 2nd 3rd and 4th
    for i in range(3):
        checklist = findNum(string, checklist,i)
    # plist(checklist)

    #check if length matches original string + 3 periods
    output = []

    for ip in checklist:
        if len(ip) == len(string) + 3:
            output.append(ip)
    

    # print("len(output)",len(output))
    plist(output)
    return output


def find1stnum(string):
    checklist1 = []
    startidx = 1
    endidx = startidx + 3
    for i in range(1,4):
        if i > len(string):
            continue
        if isValidNum(string[0:i]):
            checklist1.append(string[0:i])
    return checklist1

def findNum(string, checklist, periods):
    newChecklist = []
    currChecks = []
    for i in range(len(checklist)):
        stringSoFar = checklist[i]
        startidx = len(stringSoFar) - periods
        endidx = startidx + 3
        # print("stringSoFar: {}, examine string[startidx]:{}".format(stringSoFar,string[startidx]))

        for j in range(startidx,endidx):
            if j+1 > len(string):
                continue
            # print("jLoop {}.".format(checklist[i]),string[startidx:j+1])
            if isValidNum(string[startidx:j+1]):
                currChecks.append(string[startidx:j+1])

        print("J Loop complete {}.".format(checklist[i]), currChecks)
        for num in currChecks:
            newChecklist.append(stringSoFar + "." + num)
        currChecks = [] #clears currChecks before going to next checklist[i]
    return newChecklist

def isValidNum(string):
    if len(string) == 0:
        return False
    if len(string) >= 2:
        if string[0] == "0":
            return False
    num = int(string)
    if 0 <= num <= 255:
        return True
    else:
        return False

def plist(list):
    for ip in list:
        print(ip)

beep = "1921680"
# print(isValidNum(beep))
validIPAddresses(beep)

""" 
    #find second number
    secondnum = []
    checklist2 = []
    for i in range(len(checklist1)):
        numTemp = checklist1[i]
        startidx = len(numTemp)
        endidx = startidx + 3
        for j in range(startidx,endidx):
            if j > len(string):
                continue
            if isValidNum(string[startidx:j]):
                secondnum.append(string[startidx:j])

        for num in secondnum:
            checklist2.append(numTemp + "." + num)
        secondnum = []
        
    print("2nd", checklist2)

    #find third number
    thirdnum = []
    checklist3 = []
    for i in range(len(checklist2)):
        numTemp = checklist2[i]
        startidx = len(numTemp) - 1 #subtract bc of addding "."
        endidx = startidx + 3   
        for j  in range(startidx,endidx):
            if j > len(string):
                continue
            if isValidNum(string[startidx:j]):
                thirdnum.append(string[startidx:j])
        
        for num in thirdnum:
            checklist3.append(numTemp + "." + num)
        thirdnum = []

    print("3rd", checklist3)

    return output"""
