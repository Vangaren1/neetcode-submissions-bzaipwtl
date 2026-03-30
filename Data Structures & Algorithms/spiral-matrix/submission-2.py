class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        height = len(matrix)
        width = len(matrix[0])
        remaining = height * width
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirPos = 0
        seen = set()
        y, x = 0, 0

        while remaining > 0:
            seen.add((y, x))
            results.append(matrix[y][x])
            remaining -= 1

            dy, dx = direction[dirPos]

            y, x = y + dy, x + dx

            if (y, x) in seen or y == height or y < 0 or x < 0 or x == width:
                y, x = y - dy, x - dx
                dirPos = (dirPos + 1) % 4
                dy, dx = direction[dirPos]
                y, x = y + dy, x + dx
        return results