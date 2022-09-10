'''
Given a set number of miles and the number of hours, calculate 
the total number of miles traveled.
https://open.kattis.com/problems/speedlimit 
🟢 1.5 Easy Difficulty
'''


def DistanceCalc(s,t):
    s = int(s)
    t = int (t)
    return s * t
n = int(input())            # number of pairs of values
while n != -1:
    tc = 0                      # Time Counted
    DC = 0
    for i in range(n):
        s, t, = input().split()
        t = int(t)
        t -= int(tc)
        tc += int(t)
        DC += DistanceCalc(s,t)

    print(DC,"miles")
    n = int(input())
    print("Test")
