def toBinary(number):
    binary = ''
    while number > 0:
        number, rem = divmod(number, 2)
        binary = str(rem) + binary
    return binary


print(toBinary(10))
