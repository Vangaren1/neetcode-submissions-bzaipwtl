class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width = len(matrix[0])

        newMatrix = [[0 for _ in range(height)] for _ in range(width)]

        for y in range(height):
            for x in range(width):
                newMatrix[x][y] = matrix[y][x]
        return newMatrix