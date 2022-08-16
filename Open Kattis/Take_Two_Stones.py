'''
The game is take two stones, given an N number 
of stones in a pile who will win Bob or Alice?

https://open.kattis.com/problems/twostones
'''
N = int(input())
if N % 2 == 0:
    print('Bob')
else:
    print('Alice')
