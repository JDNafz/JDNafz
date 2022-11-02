def validIPAddresses(string):
    output = []
    
    #find first number
    checklist1 = []
    startidx = 1
    endidx = startidx + 3
    for i in range(1,4):
        if i > len(string):
            continue
        if isValidNum(string[0:i]):
            checklist1.append(string[0:i])

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

    return output

def checkNextSet(string,checklist):
    pass





def isValidNum(string):
    if len(string) == 0:
        return False
    if len(string) > 1:
        if string[0] == "0":
            return False
    num = int(string)
    if 1 <= num <= 255:
        return True
    else:
        return False

beep = "1921680"
# print(isValidNum(beep))
validIPAddresses(beep)