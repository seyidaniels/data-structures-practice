class Solution:
    def spiralOrder(self, matrix):
        spirals = []
        spirals.extend(matrix[0])
        spirals.extend(self.getColumns(matrix))
        i = len(matrix)
        while i > 1:
            spirals.extend(self.getRows(matrix, i - 1))
            i -= 1
        return self.removeDuplicates(spirals)

    def getRows(self, matrix, row, *args, **kwargs):
        singlerow = matrix[row]
        if len(matrix) - 1 == row:
            singlerow.reverse()
        return singlerow

    def removeDuplicates(self, listofElements):
        uniques = []
        for index in listofElements:
            if index not in uniques:
                uniques.append(index)
        return uniques

    def getColumns(self, matrix):
        columns = []

        i = 0
        j = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (j == len(matrix[0]) - 1):
                    columns.append(matrix[i][j])
            # for i, x in enumerate(matrix):
            #     for j, y in enumerate(matrix[0]):
            #         if j == len(matrix) - 1:
            #             columns.append(matrix[i][j])
        return columns


solution = Solution()
data = solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(data)
