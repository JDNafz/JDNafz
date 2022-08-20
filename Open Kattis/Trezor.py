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



def slopeCalc(i,j,H,L,bankA):
    up,over = i,j
    i += up
    j += over
    while i < H and j <L:
        print("-----------------------------------------")
        print("(i,j):(",i,j,")H:",H,"L",L)
        print("-------------------------------------------")
        bankA[i][j] = 0
        print("bankA:",bankA)
        i += up
        j += over
        print("i is now",i)
        print("j is now",j)
    return bankA


def trezor(A,B,L):
    H = (A+B+1)
    banks = []
    bankA = []
    bankB = []
    #set matrix to None
    for i in range(H):
        bankA.append([None]*L)
        banks.append([None]*L)
    
    #if you find None -> slopeCalc
    for j in range(L):
        for i in range(H):
            if bankA[i][j] is None:
                bankA[i][j] = 1
                print("preSlopeCalc",i,j)
                if i!= 0 or j != 0:
                    print("---SLOPE CALC----")
                    slopeCalc(i,j,H,L,bankA)
    # print(bankA)
    for i in reversed(bankA): 
        bankB.append(i)
    # print(bankB)
    for i in range(len(bankA)):
        for j in range(len(bankA[0])):
            banks[i][j] = bankA[i][j] + bankB[i][j]

    return banks

print(trezor(1,1,3))
