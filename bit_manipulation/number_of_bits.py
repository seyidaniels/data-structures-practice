def getNumberOfBits(number):
    count = 0
    while number:
        number &= number - 1
        count += 1
    return count


def countBits(length):
    array = [0] * length

    for i in range(length):
        array[i] = getNumberOfBits(i)

    return array


p = countBits(5)
print(p)
