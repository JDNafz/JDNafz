#This code calculates the ratios of whitespace characters, 
#lowercase letters, uppercase letters, and symbols. 
#the premise is to use this data as a spam filter 
#view the full propmpt here: 
# https://open.kattis.com/problems/alphabetspam

# Difficulty 1.4 🟢 Easy





#hardcoded test
# x = str('\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!')
x = input()

whiteCounter = 0
lowerCounter = 0
upperCounter = 0 
symbolCounter = 0 
#set counters to zero ^^^

for i in range(len(x)):
    j = ord(x[i])
    if j >= 65 and j <= 90:   
        upperCounter += 1
    elif j >= 97 and j <= 122:
        lowerCounter += 1
    elif j == 95: #asci 95 is _ representing white spaces
        whiteCounter += 1 # add to the White Space Counter
    else:               #else it's a symbol
        symbolCounter += 1


print((whiteCounter / len(x)))
print((lowerCounter / len(x)))
print((upperCounter / len(x)))
print((symbolCounter / len(x)))



