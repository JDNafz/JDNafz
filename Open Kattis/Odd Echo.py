'''
Write a program that echos back every other word

https://open.kattis.com/problems/oddecho
🟢 1.3  Easy Difficulty
'''

Numberofwords = int(input())
echos = []
ignore = []
for i in range(Numberofwords):
    if i % 2 == 0:
        echos.append(input())
    else:
        ignore.append(input())
print(*echos,sep='\n')