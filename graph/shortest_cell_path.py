from collections import deque


def shortestCellPath(grid, sr, sc, tr, tc):
    R = len(grid)
    C = len(grid[0])

    queue = deque()
    queue.append((sr, sc, 0))

    visitedNodes = []
    visitedNodes.append((sr, sc))

    while queue:
        currentNode = queue.popleft()
        currentRow = currentNode[0]
        currentColumn = currentNode[1]
        currentDepth = currentNode[2]
        if currentNode[0] == tr and currentNode[1] == tc:
            return currentNode[2]
        for (newRow, newColumn) in ((currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn + 1), (currentRow, currentColumn - 1)):
            if (0 <= newRow < R and 0 <= newColumn < C and grid[newRow][newColumn] == 1 and (newRow, newColumn) not in visitedNodes):
                visitedNodes.append((newRow, newColumn))
                queue.append((newRow, newColumn, currentDepth + 1))
    return -1


data = shortestCellPath(
    [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]], 0, 0, 2, 0)
print(data)
