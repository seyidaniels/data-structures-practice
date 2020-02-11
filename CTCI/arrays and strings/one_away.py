def oneAway(string1, string2):

    def editAway(string1, string2):
        edits = 0
        i = 0
        while i < string1:
            if string1[i] != string2[i]:
                edits += 1
        return True if edits == 1 else False

    def insertRemove(string1, string2):
        index1 = 0
        index2 = 0
        while index1 < len(string1) and index2 < len(string2):
            if string1[index1] != string2[index2]:
                if index1 != index2:
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1
        return True

    if len(string1) == len(string2):
        return editAway(string1, string2)
    elif len(string1) + 1 == len(string2):
        return insertRemove(string1, string2)
    elif (len(string1) == len(string2) + 1):
        return insertRemove(string2, string1)


p = oneAway("apple", "aple")

print(p)
