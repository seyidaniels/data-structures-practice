def product(array):
    product = 1
    for p in array:
        product *= p
    result = []
    for p in array:
        result.append(product / p)
    return result


p = product([3, 2, 1])
print(p)
