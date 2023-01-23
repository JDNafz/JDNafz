"""
Make sure each bracket closes.
🔵 Medium Difficulty

https://www.algoexpert.io/questions/balanced-brackets
"""
def balancedBrackets(string):
    stack = []
    for i in range(len(string)):        
        bracket = string[i]
        if bracket != "(" and bracket != ")" and bracket != "{" and bracket != "}" and bracket != "[" and bracket != "]":
            continue
        if len(stack) != 0:
            if bracket == stack[-1]:
                stack.pop()
                continue
        if bracket == "]" or bracket == ")" or bracket == "}":
            return False
        else:
            if bracket == "(":
                stack.append(")")
            elif bracket == "{":
                stack.append("}")
            else:
                stack.append("]")
    return len(stack) == 0





#TESTS:

# s0 = "()"
# s1 = "([])(){}(())()()"
# s13 = "[((([])([]){}){}){}([])[]((())"
# s18ish = "()[]{}{"
# s18 = "aafwgaga()[]a{}{gggg"
# balancedBrackets(s18)