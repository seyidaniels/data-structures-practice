def reverseWord(string):
    words = string.split()
    masterWord = ''
    for w in words:
        masterWord += w[::-1] + ' '
    return masterWord


p = reverseWord("Hello World")
print(p)
