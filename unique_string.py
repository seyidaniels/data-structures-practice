def isUniqueString(s):
    i = 0
    isUnique = True
    while i < len(s):
        remainder = (s[i + 1:])
        if s[i] in remainder:
            isUnique = False
            break
        i = i + 1
    return isUnique


print(isUniqueString('ALPHAbeth'))
