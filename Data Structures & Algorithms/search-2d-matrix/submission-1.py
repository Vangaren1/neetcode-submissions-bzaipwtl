class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        def translate(n):
            x = n % width
            y = n // width
            return y, x

        left = 0
        right = height * width - 1

        while left <= right:
            mid = int((left + right) / 2)
            y, x = translate(mid)
            curr = matrix[y][x]
            if curr == target:
                return True
            if curr > target:
                right = mid - 1
            else:
                left = mid + 1

        return False