class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = {}

        def recurse(index, row):
            if (index, row) in memo:
                return memo[(index, row)]
            if row < 0:
                return 0
            if row == 0:
                return triangle[0][0]
            total = triangle[row][index]
            if index != 0 and index != len(triangle[row]) - 1:
                tmp = min(recurse(index - 1, row - 1), recurse(index, row - 1))
            elif index == 0:
                tmp = recurse(0, row - 1)
            elif index == len(triangle[row]) - 1:
                tmp = recurse(len(triangle[row - 1]) - 1, row - 1)
            memo[(index, row)] = total + tmp
            return total + tmp

        best = float("inf")
        rows = len(triangle)
        lastRowCount = len(triangle[-1])
        for index in range(lastRowCount):
            best = min(best, recurse(index, rows - 1))
        return best