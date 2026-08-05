class Solution:
    def totalNQueens(self, n: int) -> int:

        col = set()
        posDiag = set()
        negDiag = set()

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for c in range(n):
                if c in col or row - c in posDiag or row + c in negDiag:
                    continue

                col.add(c)
                posDiag.add(row - c)
                negDiag.add(row + c)

                backtrack(row + 1)

                col.remove(c)
                posDiag.remove(row - c)
                negDiag.remove(row + c)

        backtrack(0)

        return count