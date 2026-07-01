class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.sumMatrix = [
            [0 for _ in range(self.width + 1)] for _ in range(self.height + 1)
        ]
        for y in range(self.height):
            for x in range(self.width):
                self.sumMatrix[y + 1][x + 1] = (
                    matrix[y][x]
                    + self.sumMatrix[y + 1][x]
                    + self.sumMatrix[y][x + 1]
                    - self.sumMatrix[y][x]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sumMatrix[row2 + 1][col2 + 1]
            - self.sumMatrix[row1][col2 + 1]
            - self.sumMatrix[row2 + 1][col1]
            + self.sumMatrix[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)