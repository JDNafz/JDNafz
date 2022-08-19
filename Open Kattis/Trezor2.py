'''
Difficulty 5.5 - Hard

Mirko decided to open a new business—bank vaults. A branch of the 
bank can be visualized in a plane, vaults being points in the plane. 
Mirko’s branch contains exactly L*(A + 1 + B) vaults, so that each point with 
integer coordinates inside the rectangle with corners (1, -A) and (L,B) contains 
one vault.

The vaults are watched by two guards—one at , the other at . A guard 
can see a vault if there are no other vaults on the line segment 
connecting them.

A vault is not secure if neither guard can see it, secure if only 
one guard can see it and super-secure if both guards can see it. Given
A, B and L, output the number of insecure, secure and super-secure vaults.

Input
The first line contains integers A and B separated by a space (1 <= A <= 2000, 1 <= B <= 2000). The 
second line contains the integer L (1 <= L <= 1,000,000,000).

Output
Output on three separate lines the numbers of insecure, secure and super-secure vaults.

https://open.kattis.com/problems/trezor
'''

'''
TODO: 
-Add input functionality
-Add proper Output
-Calculate ancestors

'''


slopes = {} #all starting points to calculate from
slopesA = {} #Edge cases from guard's persepctive from A
slopesB = {} #Edge cases from guard's persepctive from B
superSecure = 0
secure = 0

def addFromA(i,j):
    global superSecure
    global secure
    if (i,j) in slopes:
        if slopes[i,j] == "B":
            slopes[i,j] = "&"
            superSecure += 1
            secure -= 1
    else:
        secure += 1
        slopes[i,j] = "A"
def addFromB(i,j):
    global superSecure
    global secure
    if (i,j) in slopes:
        if slopes[i,j] == "A":
            slopes[i,j] = "&"
            superSecure += 1
            secure -= 1
    else:
        secure += 1
        slopes[i,j] = "B"

#finds edge cases that add up to an odd number
def slopesCalc(A,B,L):
    print("x range:", L)
    print("y range:", A+B+1)
    # for x in range(L-1):
    #     print(x+1)
    for y in range(-A,B):
        print("",y)




def trezorSecurity(A,B,L):
    print("running...")

    slopesCalc(A,B,L)


    totalBanks = (A + 1 + B)*L
    insecure = totalBanks - superSecure - secure
    # for values in slopes:
    #     if value == 1:
    #         secure += 1


    # print(insecure)
    # print(secure)
    # print(superSecure)  
    # print(slopes)



trezorSecurity(0,5,5)
# print(slopesA)
# print(slopesB)

# findEdgeCases(0,10,20)

