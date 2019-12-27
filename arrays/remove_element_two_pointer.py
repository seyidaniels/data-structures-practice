def removeElementWithPointer(array, value):
    j = 0
    i = 0
    while i < len(array):
        if array[i] != value:
            array[j] = array[i]
            j += 1

        i += 1
    print(array)
    return len(array)


d = removeElementWithPointer([3, 2, 1, 2, 2, 2, 3], 3)

print(d)
