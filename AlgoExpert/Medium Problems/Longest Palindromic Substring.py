'''

🔵 Medium
https://www.algoexpert.io/questions/longest-palindromic-substring
'''

def longestPalindromicSubstring(string):
    if len(string) == 1: 
        return string
    
    longest = 0
    start = 0
    for l in range(len(string)):
        right = len(string) - 1
        match = 0
        left = l
        while left <= right:
            if string[left] == string[right]:
                #if you arrive at the same char in the middle of the string
                if left == right:
                    match +=1
                #else it's not in the middle
                else:
                    match += 2
                left += 1

            #left & right are different
            #if there was a match
            elif match > 0:
                #reset things to zero
                match = 0
                left = l
                continue
            right -= 1
        if match > longest:
            start = l
            longest = match
    print(start,longest)
    return string[start:start+longest]