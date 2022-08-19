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
def findEdgeCases(A,B,L):
    if A*B*L > 10000000:
        #print It has begun and frog
        print(r"""\
        
 $$$$$$\ $$\           $$\                                 $$\                                               
 \_$$  _|$$ |          $$ |                                $$ |                                              
   $$ |$$$$$$\         $$$$$$$\   $$$$$$\   $$$$$$$\       $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$\  
   $$ |\_$$  _|        $$  __$$\  \____$$\ $$  _____|      $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\ 
   $$ |  $$ |          $$ |  $$ | $$$$$$$ |\$$$$$$\        $$ |  $$ |$$$$$$$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |
   $$ |  $$ |$$\       $$ |  $$ |$$  __$$ | \____$$\       $$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |
 $$$$$$\ \$$$$  |      $$ |  $$ |\$$$$$$$ |$$$$$$$  |      $$$$$$$  |\$$$$$$$\ \$$$$$$$ |\$$$$$$  |$$ |  $$ |
 \______| \____/       \__|  \__| \_______|\_______/       \_______/  \_______| \____$$ | \______/ \__|  \__|
                                                                               $$\   $$ |                    
                                                                               \$$$$$$  |                                       
           .--._.--.
          ( O     O )
          /   . .   \
         .`._______.'.
        /(           )\
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\
         '-'|/   \|`-`
                        """)
        
    slopesA = {} #Edge cases from guard's persepctive from A
    slopesB = {} #Edge cases from guard's persepctive from B
    slopesC = {}
    slopesD = {}
    slopesE = {}

    #from persepctive of A
    atemp = -A + 2
    i,j = 3 ,atemp
    while i <= L:
        while -A <= j <= B:
            addFromA(i,j)
            slopesC[i,j] = 1    
            j += 2
        i +=2
        j = atemp

    #from persepctive of B
    btemp = B - 2
    i,j = 2, btemp
    while 2 <= i <= L:
        # while -A <= j <= B:
        #     addFromB(i,j)
        #     slopesE[i,j] = 1
        #     j += 1
        while -A+1 <= j <= B:
            addFromB(i,j)
            slopesD[i,j] = 1
            j -= 2
        i += 1
        j =btemp

    print("C",slopesC)
    print("D", slopesD)
    return slopes

def findCommonCases(A,B,L):
    #find (1,-A) - (1,B) from A 
    i,j = 1 , -A
    while j <= B:
        addFromA(i,j)
        slopesA[i,j] = 1 
        j+= 1
    i, j = 2 , -A + 1
    
    #find  (1, -A+1) to (L, -A+1) from A
    #i needs to start at 2, to not hit the point already checked in column1
    i,j = 2, -A + 1
    while i <= L:
        addFromA(i,j)
        slopesA[i,j] = 1 
        i+= 1
    i, j = 2 , B - 1
    
    # from (1,B) to (1,-A) from B
    i,j = 1 , -A
    while j <= B:
        addFromB(i,j)
        slopesB[i,j] = 1
        j+= 1

    # find to from (2,B-1)(L,B-1)  from B
    #i needs to start at 2, to not hit the point already checked in column1  
    i,j = 2 , B - 1      
    while i <= L:
        addFromB(i,j)
        slopesB[i,j] = 1
        i+=1
    return slopes

def trezorSecurity(A,B,L):
    print("running...")
    slopes.update(findEdgeCases(A,B,L))
    slopes.update(findCommonCases(A,B,L))
    totalBanks = (A + 1 + B)*L
    insecure = totalBanks - superSecure - secure
    # for values in slopes:
    #     if value == 1:
    #         secure += 1


    print(insecure)
    print(secure)
    print(superSecure)  
    print(slopes)



trezorSecurity(1,1,3)
# print(slopesA)
# print(slopesB)

# findEdgeCases(0,10,20)










# ------------------------------- tests -----------------------------------------------

def test(testNum):
    #sample 1
    if testNum == 0:
        tests = [1,2,3]      
        for i in   tests:
            test(i)
    if testNum == 1:
        if trezorSecurity(1,1,3) == 4:
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
        if trezorSecurity(2,3,4) == 16:
            print("\n************* TEST 2 PASSED ***************************")
            print("for now....")
        else:
            print("\n-------------- TEST 2 FAILED -------------- ")
#     Insecure: 0
#       Secure: 16
# Super-secure: 8

    #sample 3
    if testNum == 3:
        if trezorSecurity(7, 11, 1000000) == 9025139:
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

