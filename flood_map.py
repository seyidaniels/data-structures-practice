def findHighPoint(map):
    R = len(map)
    C = len(map[0])
    newArray = [[0 for col in range(C)] for row in range(R)]
    for i in range(R):
        for j in range(C):
            current = map[i][j]
            isTrue = True
            for x in (0, 1, -1):
                for y in (0, -1, 1):
                    if x == 0 and y == 0:
                        continue
                    else:
                        if (0 <= x + i < R) and (0 <= y + j < C):
                            if current <= map[x + i][y + j]:
                                isTrue = False
            if isTrue:
                newArray[i][j] = 1
    return newArray


p = findHighPoint([
    [1, 2, 1, 3, 4],
    [1, 5, 2, 2, 2],
    [4, 5, 1, 9, 7],
    [3, 5, 3, 7, 6],
    [4, 3, 1, 7, 3]
])

print(p)
