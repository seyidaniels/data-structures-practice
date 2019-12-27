def oneAway(string1, string2):
    res = set(string1).intersection(string2)
    edits = 0
    for s in string1:
        if s not in res:
            edits += 1

    return True if edits == 1 else False


p = oneAway("apple", "aple")

print(p)
