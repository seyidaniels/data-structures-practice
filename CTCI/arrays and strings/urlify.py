def urlify(string, length):

    #  Count length of spaces needed
    spaceCount = 0
    for i in range(length):
        if (string[i] == ' '):
            spaceCount += 1

    index = length + spaceCount * 2

    newString = ''

    for i in range(length):
        if (string[i] == ' '):
            newString += '%20'
        else:
            newString += string[i]

    return newString

    # print(string)

    # for s in string:
    #     if s == ' ':
    #         newString += "%20"
    #     else:
    #         newString += s

    # return newString


p = urlify('Mr John Smith    ', 13)

print(p)
