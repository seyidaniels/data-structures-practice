from functools import reduce
data = [2, 4, 6, 8, 12, 15]

newData = map(lambda value: value * value, data)

# print(newData)
numbers = [1, 2, 3, 4, 5, 6]


newNumbers = filter(lambda number: number % 2 == 1, numbers)

newNumbers = map(lambda number: number * number, newNumbers)

sum = reduce(lambda number, total: number + total, newNumbers)


print(newNumbers)
print(sum)
