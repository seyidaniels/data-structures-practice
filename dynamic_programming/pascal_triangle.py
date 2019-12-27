def pascalTriangle(number):
    triangle = list()
    for r in range(number):
        row = [None for x in range(r + 1)]
        row[0] = 1
        row[-1] = 1
        for j in range(1, len(row) - 1):
            previous = triangle[r - 1]
            row[j] = previous[j - 1] + previous[j]
        triangle.append(row)
    return triangle
