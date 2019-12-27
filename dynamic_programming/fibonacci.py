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


# fib = fibonacci(35)
memo_fibonacci = memo_fibonacci(35)

print(memo_fibonacci)
# print(fib)
