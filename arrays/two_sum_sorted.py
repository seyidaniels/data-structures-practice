def getSum(array, target):
    i = 0
    j = len(array) - 1

    while i < len(array):
        if array[i] + array[j] == target:
            return [i, j]
        if array[i] + array[j] > target:
            j -= 1
        else:
            i += 1


p = getSum([2, 4, 8, 10, 14, 20, 26], 24)

print(p)
