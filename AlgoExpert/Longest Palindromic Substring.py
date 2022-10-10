def longestPalindromicSubstring(string):
    longest = 0
    start = 0
    for i in range(len(string)):
        new = checkHere(i, string)
        if new > longest:
            start = i
            longest = new
    print(start,longest)
    final = string[start:start+longest]
    print(final)
    return final

    
def checkHere(left,string):
    right = len(string) - 1
    end = right
    match = 0
    while left <= right:
        # print(left,end)
        if string[left] == string[right]:
            if match == 0:
                end = right
            if left == right:
                match +=1
            else:
                match += 2
            right -= 1
            left += 1
        else:
            match = 0
            right -= 1
    return match
    




a = "abaxyzzyxf"
b = "ab12365456321bb"
longestPalindromicSubstring(b)