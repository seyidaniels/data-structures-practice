# Without using additional Data Structures
def isUnique(string):
    i = 0
    while i < len(string):
        current = string[i]
        if current in string[i + 1:]:
            return False
        i += 1
    return True


#  Using Hash Table
def isUniqueUsingHashTable(string):
    # If it is an ASCII character set, Return False

    if len(string) > 128:
        return False

    map = {}
    for s in string:
        if s in map:
            return False
        map[s] = True
    return True


d = isUniqueUsingHashTable('mad')


# Time Complexity of this Problem is 0(N)
print(d)
