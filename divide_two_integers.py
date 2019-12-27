import sys


def divide(dividend, divisor):

    isNegative = True if (dividend < 0) != (divisor < 0) else False

    dividend, divisor = abs(dividend), abs(divisor)

    summ = divisor
    quotient = 0

    if dividend >= 2 ** 31 - 1:
        return 2 ** 31 - 1

    while summ <= dividend:
        current_quotient = 1
        while (summ + summ) <= dividend:
            summ += summ
            current_quotient += current_quotient

        dividend -= summ
        summ = divisor
        quotient += current_quotient

    return -quotient if isNegative else quotient


p = divide(-2147483648, -1)

print(p)
