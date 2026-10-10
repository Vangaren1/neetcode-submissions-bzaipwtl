class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set( i for i in range(1, n*n+1))
        results = []
        for row in grid:
            for i in row:
                if i not in nums:
                    results.append(i)
                    continue
                nums.remove(i)
        results.append(nums.pop())
        return results
