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
Made some good progress on Trezor. 
Looked at calculating lines approaching the top. 
Need to look at lines approaching the far side. 

'''



def insecureCalc(A,B,L):
    height = abs(A-(-B)) 
    # if even number or odd number
    if height % 2 == 0:
        rangecalc = int(height/2)
    else:
        rangecalc = int(height/2)+1

    insecurePoints = 0 
    for i in range(rangecalc):
        print("Loop#",i)
        if i == 0:
            insecurePoints += 2*(L-1)
            print("+", (L-1))
        else:
            insecurePoints += 2*((height//i)-1)
            print("+",(height//i)-1)
    print("height:",height)
    print("rangecalc", rangecalc)
    print("InsecurePoints:", insecurePoints)
        
    
    return insecurePoints


def findSlopes(A,B,L):
    height = abs(A-(-B))
    slopes = {} 
    slopesA = {}
    slopesB = {}

    atemp = -A + 2
    i,j = 3 ,atemp
    while i <= L:
        while -A <= j <= B:
            slopes[i,j] = 1 #enter them as Dict[touple] = key
            slopesA[i,j] = 1
            j += 2
        i +=2
        j = atemp

    btemp = B - 2
    i,j = 3, btemp
    while 0 <= i <= L:
        while -A <= j <= B:
            if (i,j) in slopes:
                slopes[i,j] += 1
                slopesA[i,j] = 1 
            else:
                slopes[i,j] = 1
            slopesB[i,j] = 1 
            j -= 2
        i += 2
        j =btemp



    print(slopesA)


findSlopes(10,0,10)









# ------------------------------- tests -----------------------------------------------

def test(testNum):
    #sample 1
    if testNum == 0:
        tests = [1,2,3]      
        for i in   tests:
            test(i)
    if testNum == 1:
        if insecureCalc(1,1,3) == 4:
            print("\n************* TEST 1 PASSED ***************************")
            print("for now....")
        else: 
            print("\n-------------- TEST 1 FAILED -------------- ")
        # Answers:
        #     Insecure: 2
        #       Secure: 2
        # Super-secure: 5

    #sample 2
    if testNum == 2:
        if insecureCalc(2,3,4) == 16:
            print("\n************* TEST 2 PASSED ***************************")
            print("for now....")
        else:
            print("\n-------------- TEST 2 FAILED -------------- ")
#     Insecure: 0
#       Secure: 16
# Super-secure: 8

    #sample 3
    if testNum == 3:
        if insecureCalc(7, 11, 1000000) == 9025139:
            print("\n************* TEST 3 PASSED ***************************")
            print("for now....")
        else:
            print("\n-------------- TEST 3 FAILED -------------- ")
            print("inscureCalc returned", insecureCalc(7, 11, 1000000),"but expected", 9025139, "\n a difference of ",9025139 - insecureCalc(7, 11, 1000000))
#     Insecure: 6 723 409
#       Secure: 2 301 730
# Total insecure:       9025139
# Super-secure: 9 974 861





#test all:
# test(0)

