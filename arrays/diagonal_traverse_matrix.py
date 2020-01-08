def findDiagonalOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])

    result = []
    for k in range(m):
        j = 0
        i = k
        while i >= 0:
            result.append(matrix[i][j])
            i -= 1
            j += 1
    return result


p = findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(p)
