def factorial(number):
    if number == 0:
        return 1
    else:
        return (number * factorial(number - 1))


print(factorial(4))
