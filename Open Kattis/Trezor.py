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
# ROW COL
# i   j 
def slopeCalc():
    pass

def trezor(A,B,L):
    H = (A+B+1)
    banks = [0,0,0]
    # for i in range(H):
    #     banks.append([None]*L)

    # for j in range(L):
    #     for i in range(H):
    #         if banks[i][j] is None:
    #             banks[i][j] = 1
    #             slopeCalc(i,j)
    bankB = [1,2,5]
    # for i in reversed(banks): 
    #     bankB.append(i)

    for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

    print(banks)

trezor(0,3,5)