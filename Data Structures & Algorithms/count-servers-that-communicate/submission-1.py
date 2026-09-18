class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        counted = set()
        height = len(grid)
        width = len(grid[0])

        for y in range(height):
            tmpset = set()
            for x in range(width):
                if grid[y][x] == 1:
                    tmpset.add((y, x))
            if len(tmpset) >= 2:
                for pos in tmpset:
                    counted.add(pos)

        for x in range(width):
            tmpset = set()
            for y in range(height):
                if grid[y][x] == 1:
                    tmpset.add((y, x))
            if len(tmpset) >= 2:
                for pos in tmpset:
                    counted.add(pos)

        return len(counted)