'''
Assuming S = (R1 + R2)/2 help solve for R2 given
the values of R1 and S

https://open.kattis.com/problems/r2
'''
R1, S = input().split()
R2 = int(S) * 2 - int(R1)
print(R2) 