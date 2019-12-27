def urlify(string):
    newString = ''
    for s in string:
        if s == ' ':
            newString += "%20"
        else:
            newString += s

    return newString


p = urlify('Mr John Smith')

print(p)
