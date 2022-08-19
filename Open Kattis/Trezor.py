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


slopes = {} #all starting points to calculate from
slopesA = {} #Edge cases from guard's persepctive from A
slopesB = {} #Edge cases from guard's persepctive from B

#calculates roughly how many insecure exist total:
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

def addPoint(i,j):
    if (i,j) in slopes:
        slopes[i,j] += 1
    else:
        slopes[i,j] = 1


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

    atemp = -A + 2
    i,j = 3 ,atemp
    while i <= L:
        while -A <= j <= B:
            addPoint(i,j)
            slopesA[i,j] = 1 
            j += 2
        i +=2
        j = atemp

    btemp = B - 2
    i,j = 3, btemp
    while 0 <= i <= L:
        while -A <= j <= B:
            addPoint(i,j)
            slopesB[i,j] = 1 
            j -= 2
        i += 2
        j =btemp


    return slopes
    print(slopes)

def findCommonCases(A,B,L):
    slopes.update(findEdgeCases(A,B,L))

    #find (1,-A) - (1,B) from A perspective
    i,j = 1 , -A
    while j <= B:
        addPoint(i,j)
        slopesA[i,j] = 1 
        j+= 1
    i, j = 2 , -A + 1
    
    #find  (1, A+1) to (L, A+1) from A
    while i <= L:
        addPoint(i,j)
        slopesA[i,j] = 1 
        i+= 1
    i, j = 2 , B - 1
    
    # from (1,B) to (1,-A)
    i,j = 1 , -A
    while j <= B:
        addPoint(i,j)
        slopesB[i,j] = 1 
        j+= 1
    # find to L,B-1 from B
    while i <= L:
        addPoint(i,j)
        slopesB[i,j] = 1
        i+=1


findCommonCases(1,1,3)
# print(slopes)
# print(slopesA)
print(slopesB)

# findEdgeCases(0,10,20)










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

