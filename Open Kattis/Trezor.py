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
x think this is broken. working on trezor2.py instead


'''


slopes = {} 
slopesA = {}
slopesB = {}

superSecure = 0
secure = 0

def addFromA(x,y):
    global superSecure
    global secure
    if (x,y) in slopes:
        if slopes[x,y] == "B":
            slopes[x,y] = "&"
            superSecure += 1
            secure -= 1
    else:
        secure += 1
        slopes[x,y] = "A"
def addFromB(x,y):
    global superSecure
    global secure
    if (x,y) in slopes:
        if slopes[x,y] == "A":
            slopes[x,y] = "&"
            superSecure += 1
            secure -= 1
    else:
        secure += 1
        slopes[x,y] = "B"

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

    #from persepctive of A
    atemp = -A + 2
    x,y = 3 ,atemp
    while x <= L:
        while -A <= y <= B:
            addFromA(x,y)
            slopesA[x,y] = "A1"    
            y += 2
        x +=2
        y = atemp

    #from persepctive of B
    btemp = B - 2
    x,y = 2, btemp
    while 2 <= x <= L:
        while -A <= y <= B:
            addFromB(x,y)
            slopesB[x,y] = "B1"
            y += 1
        while -A+1 <= y <= B:
            addFromB(x,y)
            slopesB[x,y] = "B2"
            y -= 2
        x += 1
        y =btemp

    # print("C",slopesC)
    # print("D", slopesD)
    return slopes

def findCommonCases(A,B,L):
    #find (1,-A) - (1,B) from A 
    x,y = 1 , -A
    while y <= B:
        addFromA(x,y)
        slopesA[x,y] = "A2" 
        y += 1
    x, y = 2 , -A + 1
    
    #find  (1, -A+1) to (L, -A+1) from A
    #x needs to start at 2, to not hit the point already checked in column1
    x,y = 2, -A + 1
    while x <= L:
        addFromA(x,y)
        slopesA[x,y] = "A3"
        x += 1
    x, y = 2 , B - 1
    
    # from (1,B) to (1,-A) from B
    x,y = 1 , -A
    while y <= B:
        addFromB(x,y)
        slopesB[x,y] = "B3"
        y += 1

    # find to from (2,B-1)(L,B-1)  from B
    #x needs to start at 2, to not hit the point already checked in column1  
    x,y = 2 , B - 1      
    while x <= L:
        addFromB(x,y)
        slopesB[x,y] = "B4"
        x +=1
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


    print("Insecure:",insecure)
    print("secure:",secure)
    print("superSecure:",superSecure)  
    print(slopesB)


trezorSecurity(0,6,6)

# print(slopesB)
# problemchildren = slopesB.get((2,1))
# print(problemchildren)

'''
#THIS IS NOT WORKING TO GET THE KEY
# ampersand = []
# for key,value in slopes:
#     if value == "&":
#         print("yup")
#         ampersand.append(key,value)
# print(ampersand)
'''


