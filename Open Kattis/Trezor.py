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
# ROW   COL
# i     j j j j j j j j j j j j 
# i
# i
# i
# i
import time

def slopeCalc(i,j,H,L,bankA):
    up,over = i,j+1
    i += up
    j += over
    # print("Increments by over",over,"and up:",up)    
    while i < H and j < L:
        # print("(j,i)(",j,",",i,") SET TO 0")
        bankA[i][j] = 0
        i += up
        j += over
    return bankA


def trezor(A = None, B = None, L = None):
    if A == None and B == None and L == None:
        inString = input().split()
        A, B = int(inString[0]), int(inString[1])
        L = int(input())

    H = (A+B+1)
    banks, bankA,bankB,insecure, secure, superSecure = [],[],[],0,0,0
    #set matrix to None
    for i in range(H):
        bankA.append([None]*L)
        banks.append([None]*L)
    
    #if you find None -> slopeCalc
    for j in range(L):
        for i in range(H):
            if bankA[i][j] is None:
                # set point to 1 meaning secure!
                bankA[i][j] = 1

                # print("slopeCalc([",i,"][",j,"])")
                #set obscured to 0
                slopeCalc(i,j,H,L,bankA)
    for i in reversed(bankA): 
        bankB.append(i)
    # print(bankB)
    for i in range(len(bankA)):
        for j in range(len(bankA[0])):
            banks[i][j] = bankA[i][j] + bankB[i][j]
            if banks[i][j] == 0:
                insecure += 1
            elif banks[i][j] == 1:
                secure += 1
            else:
                superSecure +=1
    print(insecure, secure, superSecure,sep="\n")
    # return insecure, secure, superSecure


trezor(7,11,1000000)
print(time.process_time())


# print(time.process_time(trezor(7,11,11)))

# Test 3 results
# 6723409
# 2301730
# 9974861
# 7.703125 SECONDS! Needs to be under 1