def hourGlass (array):
    maxSum = 0
    for i in range(len(array) - 2):
        for j in range(len(array[0])- 2):
            singleMax = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
            maxSum = max(singleMax, maxSum)
    return maxSum
print(hourGlass([
    [0,1,0, 1,0,1],
    [1,0,1,0,1,1],
    [1,1,0,0,0,1],
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [1,0,1,0,1,0]
]))