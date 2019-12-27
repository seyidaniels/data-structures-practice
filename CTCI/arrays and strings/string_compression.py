def compressString(string):
    current = string[0]
    count = 0
    newString = ''

    for s in string:
        if current == s:
            count += 1
        else:
            newString += current + str(count)
            current = s
            count = 1

    newString += current + str(count)

    return newString if len(newString) < len(string) else string


p = compressString('aabcccccaaa')

print(p)
