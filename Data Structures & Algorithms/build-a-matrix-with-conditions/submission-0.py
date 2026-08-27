class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:

        results = [[0 for _ in range(k)] for _ in range(k)]
        rowMap = defaultdict(list)
        for above, below in rowConditions:
            rowMap[above].append(below)
        colMap = defaultdict(list)
        for left, right in colConditions:
            colMap[left].append(right)

        visitedRow = set()
        visitedCol = set()
        pathRow = set()
        pathCol = set()

        def dfs(n: int, map: defaultdict, rowOrColOrder: list, path: set, visited: set):
            if n in path:
                return False
            if n in visited:
                return True

            path.add(n)

            for child in map[n]:
                if not dfs(child, map, rowOrColOrder, path, visited):
                    return False
            path.remove(n)
            visited.add(n)
            rowOrColOrder.append(n)
            return True

        rowOrder = []
        colOrder = []

        # check for a loop
        for i in range(1, k + 1):
            if not dfs(i, rowMap, rowOrder, pathRow, visitedRow):
                return []
            if not dfs(i, colMap, colOrder, pathCol, visitedCol):
                return []

        rowOrder = rowOrder[::-1]
        colOrder = colOrder[::-1]

        for index in range(k):
            yVal = rowOrder[index]
            x = colOrder.index(yVal)
            results[index][x] = rowOrder[index]

        return results
