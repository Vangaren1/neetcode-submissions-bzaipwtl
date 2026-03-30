class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        squareSets = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()],
        ]
        for y in range(9):
            testSet = set()
            for x in range(9):
                curr = board[y][x]
                squareX = x // 3
                squareY = y // 3
                if curr.isdigit():
                    if (
                        curr not in testSet
                        and curr not in colSets[x]
                        and curr not in squareSets[squareY][squareX]
                    ):
                        testSet.add(curr)
                        colSets[x].add(curr)
                        squareSets[squareY][squareX].add(curr)
                    else:
                        return False

        return True