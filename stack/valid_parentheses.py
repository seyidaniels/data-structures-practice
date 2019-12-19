# Declare a  Character stack S
# Now traverse through the string expression
# If the current character is starting bracket we push to the stack
# if the current character is a closing bracket then pop from the stack
# if the POpped character matches the starting bracket then balanced else not balanced
# if there is some starting bracket left in the stack then the string is not balanced


def isValidParentheses(string):
    stack = list()

    for p in string:
        if p == '{' or p == '(' or p == '[':
            stack.append(p)
        else:
            if stack:
                lastElement = stack[-1]
                if p == '}':
                    if lastElement == '{':
                        stack.pop()
                if p == ']':
                    if lastElement == '[':
                        stack.pop()
                if p == ')':
                    if lastElement == '(':
                        stack.pop()
    return True if len(stack) == 0 else False


print(isValidParentheses("{][}"))
