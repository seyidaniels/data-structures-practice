def addNumbersWithoutAddition(number1, number2):
    while number2 != 0:
        xoring = number1 ^ number2
        anding = number1 & number2
        number2 = anding << 1
        number1 = xoring
    return number1


# def substractWithoutMinus(number1, number2):
#     while number2 != 0:
#         borrow = (~number2) & number2
#         number1 = number1 ^ number2
#         number2 = borrow << 1
#     return number1


# p = substractWithoutMinus(90, 78)


def subtract(x, y):

    # Iterate till there
    # is no carry
    while (y != 0):

        # borrow contains common
        # set bits of y and unset
        # bits of x
        borrow = (~x) & y

        # Subtraction of bits of x
        # and y where at least one
        # of the bits is not set
        x = x ^ y

        # Borrow is shifted by one
        # so that subtracting it from
        # x gives the required sum
        y = borrow << 1

    return x


x = 90
y = 13
print("x - y is", subtract(x, y))
