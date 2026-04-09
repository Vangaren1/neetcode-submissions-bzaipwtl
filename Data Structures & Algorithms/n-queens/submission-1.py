class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        columns = set()
        posDiag = set()
        negDiag = set()

        results = []

        def backtrack(row):
            if row == n:
                c = ["".join(r) for r in board]
                results.append(c)
                return
            for col in range(n):
                pDiag = row + col
                nDiag = row - col
                if col in columns or pDiag in posDiag or nDiag in negDiag:
                    continue

                columns.add(col)
                posDiag.add(pDiag)
                negDiag.add(nDiag)
                board[row][col] = "Q"

                backtrack(row + 1)

                columns.remove(col)
                posDiag.remove(pDiag)
                negDiag.remove(nDiag)
                board[row][col] = "."

        backtrack(0)
        return results