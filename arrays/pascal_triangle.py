class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = list()

        if numRows == 0:
            return triangle

        firstRow = [1]

        triangle.append(firstRow)

        i = 1
        while i < numRows:
            previousRow = triangle[i-1]
            currentRow = list()
            currentRow.append(1)
            j = 1
            while j < i:
                currentRow.append(previousRow[j] + previousRow[j-1])
                j += 1

            currentRow.append(1)
            triangle.append(currentRow)
            i += 1

        return triangle
