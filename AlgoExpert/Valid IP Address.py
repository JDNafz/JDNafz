'''
Find all possible valid IP Addresses from a given string of numbers.

🔵 Medium
https://www.algoexpert.io/questions/valid-ip-addresses 
'''


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
    
    # plist(output)
    return output

def find1stnum(string):
    checklist1 = []
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

        for j in range(startidx,endidx):
            if j+1 > len(string):
                continue
            if isValidNum(string[startidx:j+1]):
                currChecks.append(string[startidx:j+1])

        # print("J Loop complete {}.".format(checklist[i]), currChecks)   # Use to check combinations being added to previous string
        for num in currChecks:
            newChecklist.append(stringSoFar + "." + num)
        currChecks = []
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


#Running a test:
beep = "1921680"
validIPAddresses(beep)
