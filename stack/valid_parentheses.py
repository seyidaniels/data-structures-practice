
def isValidParentheses(string):
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = list()
    for char in string:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return True if len(stack) == 0 else False


print(isValidParentheses("(])"))
