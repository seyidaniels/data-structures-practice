def lengthOfLongestSubstring(strings: str) -> int:
    if len(strings) == 0:
        return 0
    i = 0
    j = 0
    maxLength = 0
    dicts = {}
    while i < len(strings):
        if strings[i] in dicts:
            del dicts[strings[j]]
            j += 1
        else:
            dicts[strings[i]] = True
            maxLength = max(maxLength, len(dicts.keys()))
            i += 1
    return maxLength


p = lengthOfLongestSubstring("au")

print(p)
