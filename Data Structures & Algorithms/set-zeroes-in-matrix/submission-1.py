class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])

        def setRowCol(row, col):
            matrix[row] = [0] * width
            for y in range(height):
                matrix[y][col] = 0

        zeros = []
        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 0:
                    zeros.append((y, x))
        for y, x in zeros:
            setRowCol(y, x)