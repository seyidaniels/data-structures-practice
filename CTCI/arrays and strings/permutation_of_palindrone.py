def isPalindromePermutation(string):
    string = string.replace(' ', '')
    dicts = {}
    for i in string:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    foundOdd = False
    for d in dicts:
        number = dicts[d]
        if (number % 2 == 1):
            if foundOdd:
                return False
            foundOdd = True
    return True


p = isPalindromePermutation('tact coa')
print(p)
