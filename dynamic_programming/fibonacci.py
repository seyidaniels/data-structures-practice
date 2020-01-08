from datetime import datetime


def fibonacci(number):
    if number == 1 or number == 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number-2)

# Memoization in place


def memo_fibonacci(number):
    memo = {}
    if number in memo:
        return memo[number]
    result = fibonacci(number - 1) + fibonacci(number - 2)
    memo[number] = result
    return result


# Tabulation Technique for Fibonacci

def tab_fibonacci(number):
    table = [None] * (number + 1)
    table[0] = 0
    table[1] = 1

    i = 2

    while i < len(table):
        table[i] = table[i - 1] + table[i - 2]
        i += 1

    return table[number]


# fib = fibonacci(40)
# memo_fibonacci = memo_fibonacci(40)

# print('memoized solution', memo_fibonacci)

# print('recursive solution', fib)
# print('tabular fibonacci', tab_fibonacci(100))


# It cook 47 seconds for a memoized fibonacci solution to work

# def my(n, m):
#     return n + m


# c = my(1, 2, 4)

# print(c)

c = datetime(1970, 1, 1).strftime('%Y-%d-%B')

print(c)
