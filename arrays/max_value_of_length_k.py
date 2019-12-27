def maxValue(array, length):
    maxValue = 0
    for i, value in enumerate(array):
        if i >= length - 1:
            maxValue = max(sum(array[i - 2: i + 1]), maxValue)
    return maxValue


p = maxValue([40, 20, 1, 7, 34], 3)

print(p)
