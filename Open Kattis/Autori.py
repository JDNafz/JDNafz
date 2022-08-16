
'''
The goal is to take a sample string like
'Knuth-Morris-Pratt'  and return only the initials 'KMP'
view full description here:
https://open.kattis.com/problems/autori
'''

stringInput = input()
stringOutput = str('')

stringOutput += stringInput[0] #Put starting capital letter into the output

for i in range(len(stringInput)):                   #iterate over whole string
    if stringInput[i] == '-':                           #find every hyphen
        stringOutput += stringInput[(i+1)]              #add the following character to the output
print(stringOutput)

# print ('Final String should be:', stringOutput) #WORKS

#Passed in Kattis


