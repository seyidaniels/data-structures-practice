number = 419
def reverseNumber(number):
    if type(number) is int and number > 0:
        reverse = 0
        while number > 0:
            divisionModulus = divmod(number, 10)
            reverse = reverse * 10 + divisionModulus[1]
            number = divisionModulus[0]
        return reverse
    else:
        return False


print(reverseNumber(number))

