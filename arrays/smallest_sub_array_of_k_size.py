def smallest(array, target):
    i = 0
    j = 0
    minSub = len(array)
    if target in array:
        return 1
    while i < len(array):
        if sum(array[j: i+1]) < target:
            i += 1
        else:
            minSub = min(minSub, i+1 - j)
            j += 1

    return minSub


p = smallest([4, 2, 2, 7, 4, 1, 2, 2, 1, 0], 8)

print(p)
