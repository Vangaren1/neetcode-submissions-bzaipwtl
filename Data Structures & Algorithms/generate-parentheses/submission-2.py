class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(s, opened, closed):
            if len(s) == 2 * n:
                results.append(s)

            if opened < n:
                dfs(s + "(", opened + 1, closed)

            if closed < opened:
                dfs(s + ")", opened, closed + 1)

        dfs("", 0, 0)

        return results