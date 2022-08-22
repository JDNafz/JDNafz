'''
Given a string of the form he…ey, print a 
string containing twice as many e’s.
https://open.kattis.com/problems/greetings2

🟢 1.3 Easy Difficulty
'''
x = input()
print(x[0],x[1:-1],x[1:-1],x[-1],sep='')