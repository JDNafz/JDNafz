def isPalindrome(string):
    # Write your code here.
    i=0
    for char in reversed(string):
        if char != string[i]:
            return False
        i += 1
    return True
        



isPalindrome("abcdcba")
