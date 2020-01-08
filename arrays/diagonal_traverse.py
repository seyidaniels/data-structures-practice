from collections import defaultdict


def findDiagonalOrder(matrix):
    if not matrix:
        return []
    listofValues = defaultdict(list)

    for i, x in enumerate(matrix):
        for j, y in enumerate(matrix[0]):
            if ((i+j) % 2 != 0):
                listofValues[i+j].append(matrix[i][j])
            else:
                listofValues[i+j].insert(0, matrix[i][j])
    data = []
    print(listofValues.values())
    for val in listofValues.values():
        data.extend(val)
    return data


p = findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(p)
